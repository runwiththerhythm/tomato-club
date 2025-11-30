# profiles/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy

from .models import Profile
from .forms import ProfileForm


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """
    Show the currently logged-in user's profile.
    """
    model = Profile
    template_name = "profile/profile_detail.html"

    def get_object(self, queryset=None):
        return self.request.user.profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    Edit the currently logged-in user's profile.
    """
    model = Profile
    form_class = ProfileForm
    template_name = "profile/profile_form.html"
    success_url = reverse_lazy("profiles:profile-detail")

    def get_object(self, queryset=None):
        return self.request.user.profile
