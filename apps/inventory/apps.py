# apps/inventory/apps.py
from django.apps import AppConfig

class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # แก้ไขจาก 'inventory' เป็น 'apps.inventory' หรือ 'inventory' ตามโครงสร้าง sys.path
    # หากใน settings.py คุณใช้ sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
    # ให้ใช้ 'inventory' เหมือนเดิมได้ แต่ต้องเช็คให้ชัวร์
    name = 'inventory'
