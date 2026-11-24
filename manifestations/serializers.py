from rest_framework import serializers
from .models import Manifestation, ManifestationImage, Participation


class ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = ["id", "participant_name", "role_info", "created_at"]


class ManifestationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManifestationImage
        fields = ["id", "image", "caption", "created_at"]


class ManifestationSerializer(serializers.ModelSerializer):
    participations = ParticipationSerializer(many=True, read_only=True)
    images = ManifestationImageSerializer(many=True, read_only=True)

    class Meta:
        model = Manifestation
        fields = [
            "id",
            "name",
            "type",
            "event_date",
            "year",
            "location",
            "description",
            "report",
            "cover_image",
            "participations",
            "images",
            "status",
            "created_at",
            "updated_at",
        ]
