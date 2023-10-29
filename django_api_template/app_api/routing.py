from django_api_template.app_api.resources import projects
from rest_framework import routers

project_router = routers.DefaultRouter()

project_router.register(r"projects", projects.ProjectsViewSet)
