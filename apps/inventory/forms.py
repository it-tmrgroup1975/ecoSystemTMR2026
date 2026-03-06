# apps/inventory/forms.py
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    stock_qty = forms.DecimalField(initial=0.00, required=False)

    class Meta:
        model = Product
        fields = ['name', 'code', 'price', 'stock_qty', 'description', 'image', 'type', 'uom']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("ชื่อสินค้าต้องมีความยาวอย่างน้อย 3 ตัวอักษร")
        return name

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if not code.isalnum() and '-' not in code:
            raise forms.ValidationError("รหัสสินค้าควรประกอบด้วยตัวอักษรและตัวเลขเท่านั้น")
        return code
