from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from rest_framework.routers import DefaultRouter

from actions.views import ActionViewSet
from awards.views import AwardViewSet
from history.views import HistoryViewSet
from manifestations.views import ManifestationViewSet

router = DefaultRouter()
router.register(r"history", HistoryViewSet, basename="api-history")
router.register(r"awards", AwardViewSet, basename="api-awards")
router.register(r"actions", ActionViewSet, basename="api-actions")
router.register(r"manifestations", ManifestationViewSet, basename="api-manifestations")

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("compte/", include("accounts.urls")),
    path("", include("core.urls")),
    path("historique/", include("history.urls")),
    path("recompenses/", include("awards.urls")),
    path("actions/", include("actions.urls")),
    path("manifestations/", include("manifestations.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    ]

