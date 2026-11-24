from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from rest_framework import viewsets

from accounts.views import admin_required
from .forms import AwardForm
from .models import Award
from .serializers import AwardSerializer


def award_list(request):
    year_filter = request.GET.get("annee", "all")
    level_filter = request.GET.get("niveau", "all")

    awards = Award.objects.filter(status="published")
    if year_filter != "all" and year_filter.isdigit():
        awards = awards.filter(year=int(year_filter))
    if level_filter in {"local", "zonal", "national", "international"}:
        awards = awards.filter(level=level_filter)

    available_years = (
        Award.objects.filter(status="published")
        .values_list("year", flat=True)
        .distinct()
        .order_by("-year")
    )

    return render(
        request,
        "public/awards.html",
        {
            "awards": awards,
            "available_years": available_years,
            "selected_year": year_filter,
            "selected_level": level_filter,
        },
    )


@admin_required
def admin_award_list(request):
    awards = Award.objects.all()
    return render(request, "admin/award_list.html", {"awards": awards})


@admin_required
def admin_award_create(request):
    if request.method == "POST":
        form = AwardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Récompense ajoutée.")
            return redirect("awards:admin_list")
    else:
        form = AwardForm()
    return render(request, "admin/award_form.html", {"form": form, "is_edit": False})


@admin_required
def admin_award_edit(request, pk):
    obj = get_object_or_404(Award, pk=pk)
    if request.method == "POST":
        form = AwardForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Récompense mise à jour.")
            return redirect("awards:admin_list")
    else:
        form = AwardForm(instance=obj)
    return render(request, "admin/award_form.html", {"form": form, "is_edit": True, "obj": obj})


@admin_required
@require_POST
def admin_award_delete(request, pk):
    obj = get_object_or_404(Award, pk=pk)
    obj.delete()
    messages.success(request, "Récompense supprimée.")
    return redirect("awards:admin_list")


class AwardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Award.objects.filter(status="published")
    serializer_class = AwardSerializer
