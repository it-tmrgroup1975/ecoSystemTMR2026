from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Company

# ลงทะเบียน Company แบบเรียบง่าย
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    # เหลือไว้แค่ 'name' หรือฟิลด์ที่คุณมีจริงๆ ใน models.py
    list_display = ('name',)
    search_fields = ('name',)

# ลงทะเบียน User โดยดึงความสามารถของ UserAdmin มาใช้
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # เพิ่มฟิลด์ Company เข้าไปในหน้าแก้ไข User ของ Django Admin
    fieldsets = UserAdmin.fieldsets + (
        ('ERP Profile', {'fields': ('company',)}),
    )
    list_display = ('username', 'email', 'company', 'is_staff')
    list_filter = ('company', 'is_staff', 'is_superuser')