# core/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # <--- เพิ่มบรรทัดนี้
from django.conf.urls.static import static # <--- และบรรทัดนี้เพื่อจัดการ Media
from users.views import ERPLoginView
from base.views import DashboardView
from django.contrib.auth.decorators import login_required

# ... ส่วน Branding ...

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', ERPLoginView.as_view(), name='login'),
    path('', login_required(DashboardView.as_view()), name='dashboard'),
    path('inventory/', include('inventory.urls')),
]

# ส่วนที่คุณเขียนไว้ตอนท้ายที่ทำให้เกิด Error
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)