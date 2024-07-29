from django import forms
from .models import *
import base64
from django.core.files.base import ContentFile

class MemberForm(forms.ModelForm):
    
    class Meta:
        model = MemberModel
        fields = ('name', 'phone_no', 'fee_amount', 'fee_date', 'picture', 'status', 'fee_status')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control'}),
            'fee_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'fee_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'fee_status': forms.Select(attrs={'class': 'form-control'}),
        }
        
        