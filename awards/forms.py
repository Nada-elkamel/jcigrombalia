from django import forms
from .models import Award


class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ["title", "year", "level", "description", "image", "status"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "year": forms.NumberInput(attrs={"class": "form-control"}),
            "level": forms.Select(attrs={"class": "form-select"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }
