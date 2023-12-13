from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class MainEntity(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    next_process_at = models.DateTimeField(default=timezone.now)
