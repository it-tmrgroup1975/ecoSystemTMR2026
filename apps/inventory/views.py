from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
import uuid
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Product
from .forms import ProductForm


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 15

    def get_template_names(self):
        # 1. ระบบ Multi-view: สลับ Template ตามค่าที่ส่งมาจาก URL (?view=...)
        view_type = self.request.GET.get('view', 'list')
        if view_type == 'kanban':
            return ['inventory/product_kanban.html']
        elif view_type == 'graph':
            return ['inventory/product_graph.html']
        return ['inventory/product_list.html']

    def get_queryset(self):
        # 2. Multi-tenancy: ดึงเฉพาะสินค้าของบริษัทตัวเองเท่านั้น
        queryset = Product.objects.filter(company=self.request.user.company)

        # 3. ระบบ Search: ค้นหาจากชื่อ หรือ รหัสสินค้า (Internal Reference)
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(code__icontains=search_query)
            )
        return queryset

    def post(self, request, *args, **kwargs):
        # ระบบ Bulk Actions: จัดการการลบและคัดลอกผ่าน Checkbox
        action = request.POST.get('action')
        selected_ids = request.POST.getlist('selected_ids')

        if selected_ids:
            # 1. กรองข้อมูลเฉพาะของบริษัทตนเองเพื่อความปลอดภัย (Security Check)
            products = Product.objects.filter(id__in=selected_ids, company=request.user.company)
            count = products.count()

            if action == 'delete':
                # ลบรายการที่เลือก
                products.delete()
                messages.success(request, f'ลบสินค้าจำนวน {count} รายการเรียบร้อยแล้ว')

            elif action == 'copy':
                # คัดลอกรายการที่เลือก
                for product in products:
                    # เก็บชื่อและรหัสเดิมไว้ก่อนล้าง pk
                    original_name = product.name
                    original_code = product.code

                    # ล้าง ID เดิมเพื่อให้ Django สร้าง Record ใหม่ (Insert แทน Update)
                    product.pk = None

                    # ปรับปรุงข้อมูลใหม่เพื่อป้องกันรหัสซ้ำ (Unique Violation)
                    product.name = f"{original_name} - copy"

                    # ใช้ UUID สั้นๆ 4 หลักต่อท้ายเพื่อให้รหัสไม่ซ้ำแน่นอน แม้จะกด copy หลายครั้ง
                    unique_suffix = str(uuid.uuid4())[:4]
                    product.code = f"{original_code}-copy-{unique_suffix}"

                    product.save()

                messages.success(request, f'คัดลอกสินค้าจำนวน {count} รายการเรียบร้อยแล้ว')
        else:
            messages.warning(request, 'กรุณาเลือกสินค้าอย่างน้อยหนึ่งรายการ')

        return HttpResponseRedirect(request.path_info)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    # ลบ fields = [...] ออก แล้วใช้แค่ form_class
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        # ตรวจสอบว่าผู้ใช้ Login และมีบริษัทผูกอยู่จริง
        if self.request.user.company:
            form.instance.company = self.request.user.company
            return super().form_valid(form)
        else:
            # กรณีไม่มีบริษัท ให้แจ้ง Error หรือจัดการตามเหมาะสม
            form.add_error(None, "ผู้ใช้รายนี้ยังไม่ได้ผูกกับบริษัทใดๆ ไม่สามารถสร้างสินค้าได้")
            return self.form_invalid(form)

    def form_invalid(self, form):
        print("===== DEBUG FORM ERRORS =====")
        print(form.errors)  # แสดงข้อผิดพลาดรายฟิลด์ใน Terminal
        print("POST DATA:", self.request.POST)  # ดูข้อมูลที่ส่งมาจาก HTML
        return super().form_invalid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    # ทำเช่นเดียวกันกับ UpdateView
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product_list')

    def get_queryset(self):
        # ป้องกันการแก้ไขสินค้าของบริษัทอื่น
        return Product.objects.filter(company=self.request.user.company)
