from django.shortcuts import render
from django.views.generic import TemplateView

from seeds.models import TomatoVariety


def home(request):
    featured_varieties = (
        TomatoVariety.objects.filter(is_active=True, is_featured=True)
        .order_by("name")[:6]
    )
    context = {
        "featured_varieties": featured_varieties,
    }
    return render(request, "home.html", context)


class MembershipView(TemplateView):
    template_name = "club/membership.html"


class AboutView(TemplateView):
    template_name = "club/about.html"


class JoinView(TemplateView):
    template_name = "club/join.html"


class ContactView(TemplateView):
    template_name = "club/contact.html"
