from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import ExternalUser

from .models import Picture


class UploadPictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['name', 'upload', 'category', 'tags', 'user']
        widgets = {
            'category': forms.RadioSelect(),
            'tags': forms.CheckboxSelectMultiple(),
            'user': forms.HiddenInput()
        }


class RegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = ExternalUser
        fields = UserCreationForm.Meta.fields
