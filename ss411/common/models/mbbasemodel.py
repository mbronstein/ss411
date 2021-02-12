from django.db import models
from uuid import uuid4
from django.conf import settings

class MbBaseModel(models.Model):
    id = models.UUIDField(default=uuid4,
                            editable=False, primary_key=True)
    rec_updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name='%(class)s_updated_by')
    rec_updated_on = models.DateTimeField(auto_now=True)
    rec_created_on = models.DateTimeField(auto_now_add=True)
    rec_created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name='%(class)s_created_by')
    rec_deleted = models.BooleanField(default=False)


    class Meta:
        abstract = True
