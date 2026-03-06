# apps/base/views.py
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from base.models import Company

User = get_user_model()


class DashboardView(LoginRequiredMixin, TemplateView):
    # ชี้ไปที่ไฟล์เนื้อหา ไม่ใช่ไฟล์โครงสร้าง
    template_name = 'base/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_users'] = User.objects.count() or 0
        context['total_companies'] = Company.objects.count() or 0

        # ส่ง Object บริษัทไปทั้งก้อน เพื่อให้เรียกใช้ .name หรือ .logo ได้ในอนาคต
        context['my_company'] = self.request.user.company
        return context
