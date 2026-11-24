from django.urls import path
from . import views

app_name = "awards"

urlpatterns = [
    path("", views.award_list, name="list"),
    path("admin/", views.admin_award_list, name="admin_list"),
    path("admin/ajouter/", views.admin_award_create, name="admin_create"),
    path("admin/<int:pk>/modifier/", views.admin_award_edit, name="admin_edit"),
    path("admin/<int:pk>/supprimer/", views.admin_award_delete, name="admin_delete"),
]
