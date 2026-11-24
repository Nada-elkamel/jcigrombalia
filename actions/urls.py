from django.urls import path
from . import views

app_name = "actions"

urlpatterns = [
    path("", views.action_list, name="list"),
    path("<int:pk>/", views.action_detail, name="detail"),
    path("admin/", views.admin_action_list, name="admin_list"),
    path("admin/ajouter/", views.admin_action_create, name="admin_create"),
    path("admin/<int:pk>/modifier/", views.admin_action_edit, name="admin_edit"),
    path("admin/<int:pk>/supprimer/", views.admin_action_delete, name="admin_delete"),
    path("admin/<int:pk>/galerie/<int:image_pk>/supprimer/", views.admin_action_image_delete, name="admin_image_delete"),
]
