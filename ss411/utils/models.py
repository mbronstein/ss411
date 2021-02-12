from django.db import models
from uuid import uuid4
from django.conf import settings

from taggit.managers import TaggableManager


class MbBaseModel(models.Model):
    id = models.UUIDField(default=uuid4,
                            editable=False, unique=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name='%(class)s_updated_by')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name='%(class)s_created_by')
    deleted = models.BooleanField(default=False)


    class Meta:
        abstract = True
