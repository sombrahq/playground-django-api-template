from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class Project(models.Model):
    clone_url = models.CharField(
        max_length=1024, verbose_name=_("Clone URL"), help_text=_("Clone URL without the credentials"), unique=True
    )

    # process
    last_process_at = models.DateTimeField(blank=True, null=True)
    next_process_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    process_success = models.BooleanField(default=True)
    process_every_minutes = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.clone_url

    def __repr__(self):
        return f"<Project url={self.clone_url}>"

    class Meta:
        verbose_name_plural = _("Projects")
