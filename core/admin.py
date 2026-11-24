from django.contrib import admin
from .models import MediaAsset, SiteSettings

admin.site.register(SiteSettings)
admin.site.register(MediaAsset)
