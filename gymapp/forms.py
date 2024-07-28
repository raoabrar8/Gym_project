from django import forms
from .models import *


class Form(forms.ModelForm):
    
    class Meta:
        model = MemberModel
        fields = ('name', 'phone_no', 'fee_amount', 'fee_date', 'picture', 'status', 'fee_status')