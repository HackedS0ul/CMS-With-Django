from django import forms 
from .models import Admins

class AdminsForm(forms.ModelForm):
    
    class Meta:
        model = Admins
        fields = [
            'name',
            'username',
            'email'
        ]
