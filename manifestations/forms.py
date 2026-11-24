from django import forms
from .models import Manifestation


class ManifestationForm(forms.ModelForm):
    class Meta:
        model = Manifestation
        fields = [
            "name",
            "type",
            "event_date",
            "year",
            "location",
            "description",
            "report",
            "cover_image",
            "status",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "type": forms.Select(attrs={"class": "form-select"}),
            "event_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "year": forms.NumberInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "report": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "cover_image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }
