from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length='20')
    password = forms.CharField(label='Password', max_length='20')