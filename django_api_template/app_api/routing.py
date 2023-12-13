from django_api_template.app_api.resources import main_entities
from rest_framework import routers

api_router = routers.DefaultRouter()

api_router.register(r"main_entities", main_entities.MainEntityViewSet)
