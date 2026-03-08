# core/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from base.views import DashboardView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from users.views import ERPLoginView, ProfileUpdateView, MyPasswordChangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', ERPLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', login_required(DashboardView.as_view()), name='dashboard'),
    path('inventory/', include('inventory.urls')),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile/password/', MyPasswordChangeView.as_view(), name='password_change'),
]

# ส่วนที่คุณเขียนไว้ตอนท้ายที่ทำให้เกิด Error
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
