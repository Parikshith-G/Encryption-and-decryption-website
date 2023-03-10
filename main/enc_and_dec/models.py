from django.db import models

# Create your models here.


class FileUpload(models.Model):
    file = models.FileField(upload_to='')
    
class Document(models.Model):
    file_path = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)