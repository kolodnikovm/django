from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Picture
from users.models import ExternalUser


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
        model = ExternalUser
        fields = UserCreationForm.Meta.fields
