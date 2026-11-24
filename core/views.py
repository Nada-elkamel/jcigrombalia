from datetime import date
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from accounts.views import admin_required
from actions.models import Action
from awards.models import Award
from history.models import History
from manifestations.models import Manifestation
from .forms import MediaAssetForm, SiteSettingsForm
from .models import MediaAsset, SiteSettings


def home(request):
    site = SiteSettings.get_solo()
    current_year = date.today().year
    years_existence = (
        current_year - site.founding_year
        if site.founding_year and site.founding_year <= current_year
        else None
    )

    published_actions = Action.objects.filter(status="published")
    published_awards = Award.objects.filter(status="published")
    published_manifestations = Manifestation.objects.filter(status="published")

    context = {
        "years_existence": years_existence,
        "actions_count": published_actions.count(),
        "awards_count": published_awards.count(),
        "manifestations_count": published_manifestations.count(),
        "latest_actions": published_actions.order_by("-action_date", "-id")[:3],
        "latest_awards": published_awards.order_by("-year", "-id")[:3],
        "latest_manifestations": published_manifestations.order_by("-event_date", "-id")[:3],
    }
    return render(request, "public/home.html", context)


@admin_required
def admin_dashboard(request):
    recent_actions = [("Action", a.title, a.status, a.updated_at) for a in Action.objects.order_by("-updated_at")[:4]]
    recent_awards = [("Récompense", w.title, w.status, w.updated_at) for w in Award.objects.order_by("-updated_at")[:4]]
    recent_manifs = [("Manifestation", m.name, m.status, m.updated_at) for m in Manifestation.objects.order_by("-updated_at")[:4]]
    recent_history = [("Historique", h.title, h.status, h.updated_at) for h in History.objects.order_by("-updated_at")[:4]]

    recent_items = sorted(
        recent_actions + recent_awards + recent_manifs + recent_history,
        key=lambda x: x[3],
        reverse=True,
    )[:8]

    context = {
        "total_actions": Action.objects.count(),
        "published_actions": Action.objects.filter(status="published").count(),
        "total_awards": Award.objects.count(),
        "published_awards": Award.objects.filter(status="published").count(),
        "total_manifestations": Manifestation.objects.count(),
        "published_manifestations": Manifestation.objects.filter(status="published").count(),
        "total_history": History.objects.count(),
        "published_history": History.objects.filter(status="published").count(),
        "total_media": MediaAsset.objects.count(),
        "recent_items": recent_items,
    }
    return render(request, "admin/dashboard.html", context)


@admin_required
def admin_media_list(request):
    section = request.GET.get("section", "all")
    assets = MediaAsset.objects.all()
    if section != "all":
        assets = assets.filter(section=section)

    if request.method == "POST":
        form = MediaAssetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Média téléversé avec succès.")
            return redirect("core:admin_media_list")
    else:
        form = MediaAssetForm()

    return render(
        request,
        "admin/media_list.html",
        {"assets": assets, "form": form, "selected_section": section},
    )


@admin_required
@require_POST
def admin_media_delete(request, pk):
    asset = get_object_or_404(MediaAsset, pk=pk)
    if asset.file:
        asset.file.delete(save=False)
    asset.delete()
    messages.success(request, "Média supprimé.")
    return redirect("core:admin_media_list")


@admin_required
def admin_settings_edit(request):
    site = SiteSettings.get_solo()
    if request.method == "POST":
        form = SiteSettingsForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            messages.success(request, "Paramètres du site enregistrés.")
            return redirect("core:admin_settings_edit")
    else:
        form = SiteSettingsForm(instance=site)

    return render(request, "admin/settings_form.html", {"form": form})
