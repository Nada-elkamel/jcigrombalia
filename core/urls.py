from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("admin-panel/", views.admin_dashboard, name="admin_dashboard"),
    path("admin-panel/medias/", views.admin_media_list, name="admin_media_list"),
    path("admin-panel/medias/<int:pk>/supprimer/", views.admin_media_delete, name="admin_media_delete"),
    path("admin-panel/parametres/", views.admin_settings_edit, name="admin_settings_edit"),
]
