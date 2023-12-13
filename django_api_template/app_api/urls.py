from django.urls import include, path
from django_api_template.app_api import routing
from rest_framework.authtoken import views

urlpatterns = [
    path("tokens/", views.obtain_auth_token),
    path("", include(routing.api_router.urls)),
]
