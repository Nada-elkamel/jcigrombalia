from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST


def is_admin_user(user) -> bool:
    return bool(user and user.is_authenticated and user.is_active and (user.is_staff or user.is_superuser))


def admin_required(view_func):
    decorated = user_passes_test(is_admin_user, login_url="accounts:login")(view_func)
    return login_required(decorated, login_url="accounts:login")


def admin_login(request):
    """Connexion réservée à l'administrateur unique. Aucune inscription publique."""
    if is_admin_user(request.user):
        return redirect("core:admin_dashboard")

    error_message = None
    identifier_value = ""

    if request.method == "POST":
        identifier_value = request.POST.get("identifier", "").strip()
        password = request.POST.get("password", "")

        UserModel = get_user_model()
        username = identifier_value
        if "@" in identifier_value:
            matched = UserModel.objects.filter(email__iexact=identifier_value).first()
            if matched:
                username = matched.username

        user = authenticate(request, username=username, password=password)
        if user is not None and is_admin_user(user):
            login(request, user)
            messages.success(request, "Connexion administrateur réussie.")
            next_url = request.GET.get("next") or "core:admin_dashboard"
            return redirect(next_url)

        error_message = "Identifiants invalides ou privilèges administrateur insuffisants."

    return render(
        request,
        "admin/login.html",
        {"error_message": error_message, "identifier_value": identifier_value},
    )


@require_POST
def admin_logout(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté en toute sécurité.")
    return redirect("core:home")
