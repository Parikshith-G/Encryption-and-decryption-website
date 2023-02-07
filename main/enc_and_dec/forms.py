from django import forms
from .models import FileUpload

class FileUploadForm(forms.Form):
    
    file=forms.FileField()
    