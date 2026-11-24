from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from rest_framework import viewsets

from accounts.views import admin_required
from .forms import ActionForm
from .models import Action, ActionImage
from .serializers import ActionSerializer


def action_list(request):
    query = request.GET.get("q", "").strip()
    year_filter = request.GET.get("annee", "all")
    category_filter = request.GET.get("categorie", "all")
    type_filter = request.GET.get("type", "all")

    actions = Action.objects.filter(status="published")
    if query:
        actions = actions.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if year_filter != "all" and year_filter.isdigit():
        actions = actions.filter(year=int(year_filter))
    if category_filter != "all":
        actions = actions.filter(category=category_filter)
    if type_filter != "all":
        actions = actions.filter(action_type=type_filter)

    published_all = Action.objects.filter(status="published")
    context = {
        "actions": actions,
        "years": published_all.values_list("year", flat=True).distinct().order_by("-year"),
        "categories": published_all.values_list("category", flat=True).distinct().order_by("category"),
        "types": published_all.values_list("action_type", flat=True).distinct().order_by("action_type"),
        "query": query,
        "selected_year": year_filter,
        "selected_category": category_filter,
        "selected_type": type_filter,
    }
    return render(request, "public/actions.html", context)


def action_detail(request, pk):
    action = get_object_or_404(Action, pk=pk, status="published")
    return render(request, "public/action_detail.html", {"action": action})


@admin_required
def admin_action_list(request):
    actions = Action.objects.all()
    return render(request, "admin/action_list.html", {"actions": actions})


@admin_required
def admin_action_create(request):
    if request.method == "POST":
        form = ActionForm(request.POST, request.FILES)
        if form.is_valid():
            action = form.save()
            for img_file in request.FILES.getlist("gallery_images"):
                ActionImage.objects.create(action=action, image=img_file)
            messages.success(request, "Action ajoutée.")
            return redirect("actions:admin_list")
    else:
        form = ActionForm()
    return render(request, "admin/action_form.html", {"form": form, "is_edit": False})


@admin_required
def admin_action_edit(request, pk):
    obj = get_object_or_404(Action, pk=pk)
    if request.method == "POST":
        form = ActionForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            action = form.save()
            for img_file in request.FILES.getlist("gallery_images"):
                ActionImage.objects.create(action=action, image=img_file)
            messages.success(request, "Action mise à jour.")
            return redirect("actions:admin_list")
    else:
        form = ActionForm(instance=obj)
    return render(request, "admin/action_form.html", {"form": form, "is_edit": True, "obj": obj})


@admin_required
@require_POST
def admin_action_delete(request, pk):
    obj = get_object_or_404(Action, pk=pk)
    obj.delete()
    messages.success(request, "Action supprimée.")
    return redirect("actions:admin_list")


@admin_required
@require_POST
def admin_action_image_delete(request, pk, image_pk):
    img = get_object_or_404(ActionImage, pk=image_pk, action_id=pk)
    img.delete()
    messages.success(request, "Photographie retirée de la galerie.")
    return redirect("actions:admin_edit", pk=pk)


class ActionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Action.objects.filter(status="published").prefetch_related("images")
    serializer_class = ActionSerializer
