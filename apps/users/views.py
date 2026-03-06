# apps/users/views.py
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class ERPLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True  # ถ้า Login อยู่แล้วให้ข้ามไป Dashboard เลย

    def get_success_url(self):
        return reverse_lazy('dashboard') # เดี๋ยวเราจะไปสร้าง URL นี้กัน