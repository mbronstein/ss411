from django.contrib import admin
from ss411.uploads.models import UploadFile

# Register your models here.

class UploadFileFormAdmin(admin.ModelAdmin):
    fields = ('description', 'file', 'comments', 'timestamp')

admin.site.register(UploadFile, UploadFileFormAdmin)
