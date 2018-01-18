from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Picture, User

class UploadPictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['picture_name', 'upload', 'category', 'tags', 'user']
        widgets = {
            'category': forms.RadioSelect(),
            'tags': forms.CheckboxSelectMultiple(),
            'user': forms.HiddenInput()
        }

class RegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields