from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from rest_framework import viewsets

from accounts.views import admin_required
from .forms import ManifestationForm
from .models import Manifestation, ManifestationImage, Participation
from .serializers import ManifestationSerializer


def manifestation_list(request):
    year_filter = request.GET.get("annee", "all")
    type_filter = request.GET.get("type", "all")

    items = Manifestation.objects.filter(status="published").prefetch_related("participations")
    if year_filter != "all" and year_filter.isdigit():
        items = items.filter(year=int(year_filter))
    if type_filter in {"zonale", "nationale"}:
        items = items.filter(type=type_filter)

    years = (
        Manifestation.objects.filter(status="published")
        .values_list("year", flat=True)
        .distinct()
        .order_by("-year")
    )

    return render(
        request,
        "public/manifestations.html",
        {
            "manifestations": items,
            "available_years": years,
            "selected_year": year_filter,
            "selected_type": type_filter,
        },
    )


def manifestation_detail(request, pk):
    item = get_object_or_404(
        Manifestation.objects.prefetch_related("participations", "images"),
        pk=pk,
        status="published",
    )
    return render(request, "public/manifestation_detail.html", {"manifestation": item})


def _save_participants_and_images(request, manifestation):
    names = request.POST.getlist("participant_name")
    roles = request.POST.getlist("participant_role")
    for idx, name in enumerate(names):
        clean_name = name.strip()
        if clean_name:
            role = roles[idx].strip() if idx < len(roles) else ""
            Participation.objects.create(
                manifestation=manifestation,
                participant_name=clean_name,
                role_info=role,
            )

    for img_file in request.FILES.getlist("gallery_images"):
        ManifestationImage.objects.create(manifestation=manifestation, image=img_file)


@admin_required
def admin_manifestation_list(request):
    items = Manifestation.objects.all()
    return render(request, "admin/manifestation_list.html", {"manifestations": items})


@admin_required
def admin_manifestation_create(request):
    if request.method == "POST":
        form = ManifestationForm(request.POST, request.FILES)
        if form.is_valid():
            manif = form.save()
            _save_participants_and_images(request, manif)
            messages.success(request, "Manifestation ajoutée.")
            return redirect("manifestations:admin_list")
    else:
        form = ManifestationForm()
    return render(request, "admin/manifestation_form.html", {"form": form, "is_edit": False})


@admin_required
def admin_manifestation_edit(request, pk):
    obj = get_object_or_404(Manifestation, pk=pk)
    if request.method == "POST":
        form = ManifestationForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            manif = form.save()
            _save_participants_and_images(request, manif)
            messages.success(request, "Manifestation mise à jour.")
            return redirect("manifestations:admin_list")
    else:
        form = ManifestationForm(instance=obj)
    return render(request, "admin/manifestation_form.html", {"form": form, "is_edit": True, "obj": obj})


@admin_required
@require_POST
def admin_manifestation_delete(request, pk):
    obj = get_object_or_404(Manifestation, pk=pk)
    obj.delete()
    messages.success(request, "Manifestation supprimée.")
    return redirect("manifestations:admin_list")


@admin_required
@require_POST
def admin_participant_delete(request, pk, part_pk):
    part = get_object_or_404(Participation, pk=part_pk, manifestation_id=pk)
    part.delete()
    messages.success(request, "Participant retiré.")
    return redirect("manifestations:admin_edit", pk=pk)


@admin_required
@require_POST
def admin_manifestation_image_delete(request, pk, image_pk):
    img = get_object_or_404(ManifestationImage, pk=image_pk, manifestation_id=pk)
    img.delete()
    messages.success(request, "Photographie retirée.")
    return redirect("manifestations:admin_edit", pk=pk)


class ManifestationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Manifestation.objects.filter(status="published").prefetch_related(
        "participations", "images"
    )
    serializer_class = ManifestationSerializer
