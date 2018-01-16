from django import forms

from .models import Picture

class UploadPictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['picture_name', 'upload', 'category', 'tags']
        widgets = {
            'category': forms.RadioSelect(),
            'tags': forms.CheckboxSelectMultiple()
        }