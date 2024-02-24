from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    doc_type = models.BooleanField(default=False)