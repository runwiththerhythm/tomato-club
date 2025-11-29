from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, "home.html")


class MembershipView(TemplateView):
    template_name = "club/membership.html"


class AboutView(TemplateView):
    template_name = "club/about.html"


class JoinView(TemplateView):
    template_name = "club/join.html"


class ContactView(TemplateView):
    template_name = "club/contact.html"
