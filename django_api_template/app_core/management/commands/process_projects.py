import logging

from django.core import paginator
from django.core.management import BaseCommand
from django_api_template.app_core import api


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
        pages = paginator.Paginator(api.get_projects_to_process(), options["page"])
        for page in pages:
            for project in page.object_list:
                try:
                    api.process_project(project)
                except Exception as e:
                    logging.exception(e)
