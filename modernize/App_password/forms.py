from django import forms
from .models import PasswordModle

class PasswordForm(forms.ModelForm):
    website = forms.TextInput()
    class Meta:
        model = PasswordModle
        fields = ["website", "username", "password","remarks"]
        widgets = {
            'website': forms.TextInput(attrs={
                'class':"form-control",
                'placeholder': "Enter website"
            }),
            'username': forms.TimeInput(attrs={
                'class':"form-control",
                'placeholder':"Enter username"
            }),
            'password':forms.PasswordInput(attrs={
                'class':"form-control",
                'placeholder':"Enter the password"
            }),
            'remarks': forms.Textarea(attrs={
                'class':"form-control",
                'placeholder':"Enter your remarks"
            })
        }

