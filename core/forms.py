from django import forms
from .models import MediaAsset, SiteSettings


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = [
            "org_name",
            "tagline",
            "founding_year",
            "hero_title",
            "hero_subtitle",
            "history_intro",
            "address",
            "email",
            "phone",
            "facebook_url",
            "instagram_url",
            "linkedin_url",
        ]
        widgets = {
            "org_name": forms.TextInput(attrs={"class": "form-control"}),
            "tagline": forms.TextInput(attrs={"class": "form-control"}),
            "founding_year": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ex: 1988"}),
            "hero_title": forms.TextInput(attrs={"class": "form-control"}),
            "hero_subtitle": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "history_intro": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "facebook_url": forms.URLInput(attrs={"class": "form-control"}),
            "instagram_url": forms.URLInput(attrs={"class": "form-control"}),
            "linkedin_url": forms.URLInput(attrs={"class": "form-control"}),
        }


class MediaAssetForm(forms.ModelForm):
    class Meta:
        model = MediaAsset
        fields = ["title", "section", "file"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Description du média"}),
            "section": forms.Select(attrs={"class": "form-select"}),
            "file": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
