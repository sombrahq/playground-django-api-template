import logging

from django.core import paginator
from django.core.management import BaseCommand
from django_api_template.app_core import internal


class Command(BaseCommand):
    help = "Analyses a project and saves the results for later usage"

    def add_arguments(self, parser):
        parser.add_argument(
            "--page",
            type=int,
            default=20,
            help="Page size",
        )

    def handle(self, *args, **options):
        pages = paginator.Paginator(internal.get_main_entities_to_process(), options["page"])
        for page in pages:
            for obj in page.object_list:
                try:
                    internal.process_main_entity(obj)
                except Exception as e:
                    logging.exception(e)
