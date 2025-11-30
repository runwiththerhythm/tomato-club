# club/views.py
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from django.views.decorators.http import require_POST

from seeds.models import TomatoVariety
from .forms import ContactForm, NewsletterSignupForm


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


class ContactView(FormView):
    template_name = "club/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("club:contact")

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        subject = form.cleaned_data.get("subject") or "Heritage Tomato Club contact form"
        message = form.cleaned_data["message"]

        full_message = (
            f"Message from: {name} <{email}>\n\n"
            f"Subject: {subject}\n\n"
            f"Message:\n{message}"
        )

        send_mail(
            subject=f"[Heritage Tomato Club] {subject}",
            message=full_message,
            from_email=getattr(settings, "DEFAULT_FROM_EMAIL", None),
            recipient_list=[getattr(settings, "DEFAULT_FROM_EMAIL", "admin@example.com")],
            fail_silently=True,  # console backend in dev anyway
        )

        messages.success(
            self.request,
            "Thanks for getting in touch. Your message has been sent and we’ll get back to you as soon as we can."
        )
        return super().form_valid(form)


class ResourcesView(TemplateView):
    """
    Read-only page for the Tomato Growing Resources hub.
    """
    template_name = "club/resources.html"


@require_POST
def newsletter_signup(request):
    """
    Handle newsletter signup from the resources page.
    Always redirects back to the resources hub.
    """
    form = NewsletterSignupForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(
            request,
            "Thanks for subscribing! We’ll send occasional seasonal tomato updates."
        )
    else:
        # Pull out the email field error if present
        if "email" in form.errors:
            # form.errors['email'] is an ErrorList – join it nicely
            error_text = " ".join(form.errors["email"])
            messages.error(request, error_text)
        else:
            messages.error(request, "Please enter a valid email address.")

    return redirect("club:resources")
