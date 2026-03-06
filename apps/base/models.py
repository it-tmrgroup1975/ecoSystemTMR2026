# apps/base/models.py
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # ใช้ auto_now_add=True แทนการใส่ default เอง
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"