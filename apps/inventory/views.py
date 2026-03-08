from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
import uuid
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from .models import Product
from .forms import ProductForm
from django.urls import reverse

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 15

    def get_template_names(self):
        view_type = self.request.GET.get('view', 'list')
        if view_type == 'kanban':
            return ['inventory/product_kanban.html']
        elif view_type == 'graph':
            return ['inventory/product_graph.html']
        return ['inventory/product_list.html']

    def get_queryset(self):
        queryset = Product.objects.filter(company=self.request.user.company)
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(code__icontains=search_query)
            )
        return queryset

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        selected_ids = request.POST.getlist('selected_ids')

        if selected_ids:
            products = Product.objects.filter(id__in=selected_ids, company=request.user.company)
            count = products.count()

            if action == 'delete':
                products.delete()
                messages.success(request, f'ลบสินค้าจำนวน {count} รายการเรียบร้อยแล้ว')
            elif action == 'copy':
                for product in products:
                    product.pk = None
                    product.name = f"{product.name} - copy"
                    product.code = f"{product.code}-copy-{str(uuid.uuid4())[:4]}"
                    product.save()
                messages.success(request, f'คัดลอกสินค้าจำนวน {count} รายการเรียบร้อยแล้ว')
        else:
            messages.warning(request, 'กรุณาเลือกสินค้าอย่างน้อยหนึ่งรายการ')

        # FIX: รักษา Query Params ทั้งหมด (view, search, page) ไว้หลัง Post
        params = request.GET.urlencode()
        redirect_url = request.path_info
        if params:
            redirect_url += f"?{params}"
        return HttpResponseRedirect(redirect_url)

class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product_list')
    success_message = "เพิ่มสินค้าใหม่เรียบร้อยแล้ว!"

    # เพิ่มเมธอดนี้เพื่อรักษาค่า URL Parameters หลังบันทึกสำเร็จ
    def get_success_url(self):
        # ดึงค่า view และ search จาก URL ปัจจุบันที่ส่งมาจากฟอร์ม
        view_type = self.request.GET.get('view', 'list')
        search_query = self.request.GET.get('search', '')

        url = reverse('product_list')
        # สร้าง URL ใหม่พร้อมแนบ Parameter กลับไป
        full_url = f"{url}?view={view_type}"
        if search_query:
            full_url += f"&search={search_query}"
        return full_url

    def form_valid(self, form):
        # ตรวจสอบว่ามีบริษัทผูกกับผู้ใช้หรือไม่ก่อนบันทึก
        if self.request.user.company:
            form.instance.company = self.request.user.company
            # เมื่อเรียก super().form_valid(form) Django จะจัดการบันทึกข้อมูลรวมถึงไฟล์รูปภาพให้โดยอัตโนมัติ
            return super().form_valid(form)
        else:
            form.add_error(None, "ผู้ใช้รายนี้ยังไม่ได้ผูกกับบริษัทใดๆ")
            return self.form_invalid(form)

class ProductUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product_list')
    success_message = "อัปเดตข้อมูลสินค้าเรียบร้อยแล้ว!"

    # เพิ่มเมธอดนี้เพื่อให้หน้า Edit ทำงานเหมือนหน้า Create
    def get_success_url(self):
        # ทำแบบเดียวกับ CreateView เพื่อให้หน้า Edit จำหน้าเดิมได้
        view_type = self.request.GET.get('view', 'list')
        search_query = self.request.GET.get('search', '')

        url = reverse('product_list')
        full_url = f"{url}?view={view_type}"
        if search_query:
            full_url += f"&search={search_query}"
        return full_url

    def get_queryset(self):
        return Product.objects.filter(company=self.request.user.company)