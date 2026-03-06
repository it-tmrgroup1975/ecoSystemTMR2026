from django.contrib.auth.models import AbstractUser
from django.db import models
from base.models import Company


class User(AbstractUser):
    # Connects users to companies (similar to Odoo, where each user must have a main company).
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        related_name='employees'
    )

    # Add fields for ERP UI.
    is_internal_user = models.BooleanField(default=True)
    phone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.company.name if self.company else 'No Company'})"
