from django import forms

from .models import User

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length='20')
    # email = forms.CharField(label='E-mail', max_length='20')
    password = forms.CharField(label='Password', max_length='20')
    # confirm_password = forms.CharField(label='Confirm Password', max_length='20')