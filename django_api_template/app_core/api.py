import typing

from django.db.models import QuerySet
from django.utils import timezone
from django_api_template.app_core import models


def get_projects_to_process() -> typing.Union[QuerySet, typing.List[models.Project]]:
    qs = models.Project.objects.filter(
        next_process_at__lt=timezone.now(),
    ).order_by("pk")

    return qs
