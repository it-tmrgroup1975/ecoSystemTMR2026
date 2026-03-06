from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"
