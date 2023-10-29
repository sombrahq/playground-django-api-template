from django_api_template.app_core import models
from rest_framework import serializers, viewsets


class _ProjectsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Project
        exclude = ["credentials_envvar"]
        read_only_fields = [
            "project_id",
            "last_process_at",
            "next_process_at",
        ]


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = _ProjectsSerializer
