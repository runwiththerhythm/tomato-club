from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import GrowDiaryEntry


class UserDiaryQuerysetMixin(LoginRequiredMixin):
    """
    Base mixin to always limit queryset to the current user.
    """

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class GrowDiaryListView(UserDiaryQuerysetMixin, ListView):
    model = GrowDiaryEntry
    template_name = "diary/diary_entry_list.html"
    context_object_name = "entries"


class GrowDiaryDetailView(UserDiaryQuerysetMixin, DetailView):
    model = GrowDiaryEntry
    template_name = "diary/diary_entry_detail.html"
    context_object_name = "entry"


class GrowDiaryCreateView(LoginRequiredMixin, CreateView):
    model = GrowDiaryEntry
    fields = ["variety", "date", "stage", "title", "notes", "photo"]
    template_name = "diary/diary_entry_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("diary:entry_detail", args=[self.object.pk])


class GrowDiaryUpdateView(UserDiaryQuerysetMixin, UpdateView):
    model = GrowDiaryEntry
    fields = ["variety", "date", "stage", "title", "notes", "photo"]
    template_name = "diary/diary_entry_form.html"

    def get_success_url(self):
        return reverse("diary:entry_detail", args=[self.object.pk])


class GrowDiaryDeleteView(UserDiaryQuerysetMixin, DeleteView):
    model = GrowDiaryEntry
    template_name = "diary/diary_entry_confirm_delete.html"
    success_url = reverse_lazy("diary:entry_list")
