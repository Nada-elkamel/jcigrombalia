from rest_framework import serializers
from .models import Action, ActionImage


class ActionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionImage
        fields = ["id", "image", "caption", "created_at"]


class ActionSerializer(serializers.ModelSerializer):
    images = ActionImageSerializer(many=True, read_only=True)

    class Meta:
        model = Action
        fields = [
            "id",
            "title",
            "description",
            "action_date",
            "year",
            "category",
            "action_type",
            "outcome",
            "cover_image",
            "images",
            "status",
            "created_at",
            "updated_at",
        ]
