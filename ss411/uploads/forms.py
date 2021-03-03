#forms.py

# posts/forms.py
from django import forms
from ss411.uploads.models import UploadFile

class UploadFileForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = ['description', 'file', 'comments']
