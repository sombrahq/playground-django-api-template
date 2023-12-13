import datetime
import typing

from django.db import transaction
from django.db.models import QuerySet
from django.utils import timezone
from django_api_template.app_core import models


def get_main_entities_to_process() -> typing.Union[QuerySet, typing.List[models.MainEntity]]:
    qs = models.MainEntity.objects.filter(
        next_process_at__lt=timezone.now(),
    ).order_by("pk")

    return qs


@transaction.atomic
def process_main_entity(obj: models.MainEntity):
    obj.next_process_at += datetime.timedelta(days=1)
    obj.save(update_fields=["next_process_at"])
