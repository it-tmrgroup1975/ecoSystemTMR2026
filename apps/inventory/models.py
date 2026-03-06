from django.db import models
from base.models import Company
from django.core.validators import MinValueValidator


class Product(models.Model):
    # เชื่อมกับบริษัท เพื่อให้แต่ละบริษัทเห็นเฉพาะสินค้าของตัวเอง
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products')

    name = models.CharField(max_length=255, verbose_name="Product Name")
    # ป้องกันรหัสสินค้าซ้ำ และต้องไม่เป็นค่าว่าง
    code = models.CharField(max_length=50, unique=True, verbose_name="Internal Reference")
    description = models.TextField(blank=True, null=True)

    # ป้องกันราคาและสต็อกติดลบด้วย MinValueValidator
    price = models.DecimalField(
        max_digits=12, decimal_places=2, default=1.00,
        validators=[MinValueValidator(0.01)]
    )
    stock_qty = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00,
        validators=[MinValueValidator(0.00)]
    )
    # เพิ่มฟิลด์เหล่านี้เพื่อให้ตรงกับหน้า Form
    PRODUCT_TYPES = [
        ('storable', 'Storable Product'),
        ('consumable', 'Consumable'),
        ('service', 'Service'),
    ]
    type = models.CharField(max_length=50, default='storable')
    uom = models.CharField(max_length=50, default='ใบ')

    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.code}] {self.name}"
