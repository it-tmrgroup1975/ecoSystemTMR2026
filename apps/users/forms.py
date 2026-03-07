from django import forms
from .models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'avatar']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'erp-input'}),
            'last_name': forms.TextInput(attrs={'class': 'erp-input'}),
            'phone': forms.TextInput(attrs={'class': 'erp-input'}),
        }