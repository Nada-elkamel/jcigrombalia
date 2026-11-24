from django.urls import path
from . import views

app_name = "manifestations"

urlpatterns = [
    path("", views.manifestation_list, name="list"),
    path("<int:pk>/", views.manifestation_detail, name="detail"),
    path("admin/", views.admin_manifestation_list, name="admin_list"),
    path("admin/ajouter/", views.admin_manifestation_create, name="admin_create"),
    path("admin/<int:pk>/modifier/", views.admin_manifestation_edit, name="admin_edit"),
    path("admin/<int:pk>/supprimer/", views.admin_manifestation_delete, name="admin_delete"),
    path("admin/<int:pk>/participants/<int:part_pk>/supprimer/", views.admin_participant_delete, name="admin_part_delete"),
    path("admin/<int:pk>/galerie/<int:image_pk>/supprimer/", views.admin_manifestation_image_delete, name="admin_image_delete"),
]
