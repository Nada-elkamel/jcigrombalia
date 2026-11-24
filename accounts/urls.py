from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("connexion/", views.admin_login, name="login"),
    path("deconnexion/", views.admin_logout, name="logout"),
]
