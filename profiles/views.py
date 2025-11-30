# profiles/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy

from .models import Profile
from .forms import ProfileForm


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """
    Show the currently logged-in user's profile.
    If it doesn't exist yet (e.g. old users), create it.
    """
    model = Profile
    template_name = "profile/profile_detail.html"

    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    Edit the currently logged-in user's profile.
    If it doesn't exist yet, create it first.
    """
    model = Profile
    form_class = ProfileForm
    template_name = "profile/profile_form.html"
    success_url = reverse_lazy("profiles:profile-detail")

    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
