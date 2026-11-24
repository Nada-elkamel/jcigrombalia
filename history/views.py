from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from rest_framework import viewsets

from accounts.views import admin_required
from .forms import HistoryForm
from .models import History
from .serializers import HistorySerializer


def history_list(request):
    filter_type = request.GET.get("filtre", "all")
    events = History.objects.filter(status="published")
    if filter_type == "presidents":
        events = events.filter(category__in=["Présidence", "Bureau"])
    elif filter_type == "events":
        events = events.filter(category="Événement")

    return render(
        request,
        "public/history.html",
        {"events": events, "filter_type": filter_type},
    )


@admin_required
def admin_history_list(request):
    events = History.objects.all()
    return render(request, "admin/history_list.html", {"events": events})


@admin_required
def admin_history_create(request):
    if request.method == "POST":
        form = HistoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Élément historique ajouté.")
            return redirect("history:admin_list")
    else:
        form = HistoryForm()
    return render(request, "admin/history_form.html", {"form": form, "is_edit": False})


@admin_required
def admin_history_edit(request, pk):
    obj = get_object_or_404(History, pk=pk)
    if request.method == "POST":
        form = HistoryForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Élément historique mis à jour.")
            return redirect("history:admin_list")
    else:
        form = HistoryForm(instance=obj)
    return render(request, "admin/history_form.html", {"form": form, "is_edit": True, "obj": obj})


@admin_required
@require_POST
def admin_history_delete(request, pk):
    obj = get_object_or_404(History, pk=pk)
    obj.delete()
    messages.success(request, "Élément historique supprimé.")
    return redirect("history:admin_list")


class HistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = History.objects.filter(status="published")
    serializer_class = HistorySerializer
