from rest_framework import serializers
from .models import Award


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = [
            "id",
            "title",
            "description",
            "year",
            "level",
            "image",
            "status",
            "created_at",
            "updated_at",
        ]
