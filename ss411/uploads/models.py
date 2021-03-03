from django.db import models
from django.urls import reverse

class UploadFile(models.Model):
    description = models.CharField(max_length=90, blank=True)
    file = models.FileField(upload_to='uploads/')
    comments = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'uploads'

    def __str__(self):
        return f"{self.file.name}: {self.description}"

    def get_absolute_url(self):
        return reverse('uploads:upload', kwargs={'id': self.id})

