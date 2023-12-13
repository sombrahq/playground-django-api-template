from django_api_template.app_core import models
from rest_framework import serializers, viewsets


class _MainEntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MainEntity
        fields = "__all__"
        read_only_fields = [
            "created_at",
            "updated_at",
        ]


class MainEntityViewSet(viewsets.ModelViewSet):
    queryset = models.MainEntity.objects.all()
    serializer_class = _MainEntitySerializer
