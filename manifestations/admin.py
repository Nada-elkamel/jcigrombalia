from django.contrib import admin
from .models import Manifestation, ManifestationImage, Participation

admin.site.register(Manifestation)
admin.site.register(Participation)
admin.site.register(ManifestationImage)
