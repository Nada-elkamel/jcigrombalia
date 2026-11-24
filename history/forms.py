from django import forms
from .models import History


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = [
            "title",
            "event_date",
            "category",
            "display_order",
            "president_name",
            "board_members",
            "description",
            "image",
            "status",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "event_date": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex: 2024 ou 15/03/2024"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "display_order": forms.NumberInput(attrs={"class": "form-control"}),
            "president_name": forms.TextInput(attrs={"class": "form-control"}),
            "board_members": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }
