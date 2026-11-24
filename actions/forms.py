from django import forms
from .models import Action


class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = [
            "title",
            "action_date",
            "year",
            "category",
            "action_type",
            "description",
            "outcome",
            "cover_image",
            "status",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "action_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "year": forms.NumberInput(attrs={"class": "form-control"}),
            "category": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex: Développement communautaire"}),
            "action_type": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex: Action civique, Formation"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "outcome": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "cover_image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }
