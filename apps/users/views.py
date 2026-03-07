# apps/users/views.py
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from .models import User
from .forms import UserProfileForm
from django.utils import timezone


class ERPLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True  # ถ้า Login อยู่แล้วให้ข้ามไป Dashboard เลย

    def get_success_url(self):
        return reverse_lazy('dashboard')  # เดี๋ยวเราจะไปสร้าง URL นี้กัน


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        # อัปเดตวันที่เปลี่ยนรหัสผ่าน
        self.request.user.password_last_changed = timezone.now()
        self.request.user.save()
        return response
