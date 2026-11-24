from django.urls import path
from . import views

app_name = "history"

urlpatterns = [
    path("", views.history_list, name="list"),
    path("admin/", views.admin_history_list, name="admin_list"),
    path("admin/ajouter/", views.admin_history_create, name="admin_create"),
    path("admin/<int:pk>/modifier/", views.admin_history_edit, name="admin_edit"),
    path("admin/<int:pk>/supprimer/", views.admin_history_delete, name="admin_delete"),
]
