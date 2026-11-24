from rest_framework import serializers
from .models import History


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = [
            "id",
            "title",
            "description",
            "event_date",
            "category",
            "president_name",
            "board_members",
            "image",
            "display_order",
            "status",
            "created_at",
            "updated_at",
        ]
