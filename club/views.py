# club/views.py
from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from django.views.decorators.http import require_POST

from seeds.models import TomatoVariety
from .forms import ContactForm, NewsletterSignupForm

import stripe
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.generic import TemplateView

from .models import MembershipTier, Membership



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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tiers = MembershipTier.objects.filter(is_active=True)
        context["free_tiers"] = tiers.filter(price_per_year__lte=0)
        context["paid_tiers"] = tiers.filter(price_per_year__gt=0)
        return context


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


@csrf_exempt
@csrf_exempt
@login_required
def create_membership_checkout_session(request, slug):
    """
    Create a Stripe Checkout Session for a paid membership tier.
    """
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=400)

    tier = get_object_or_404(MembershipTier, slug=slug, is_active=True)

    # Don’t allow Stripe checkout for free tiers
    if tier.price_per_year <= 0:
        return JsonResponse({"error": "This tier is free – no payment required."}, status=400)

    if not tier.stripe_price_id:
        return JsonResponse({"error": "No Stripe price id configured for this tier."}, status=500)

    stripe.api_key = settings.STRIPE_SECRET_KEY

    if not stripe.api_key:
        return JsonResponse({"error": "Stripe secret key is missing from settings."}, status=500)

    # Only include customer_email if we actually have one
    customer_kwargs = {}
    email = (request.user.email or "").strip()
    if email:
        customer_kwargs["customer_email"] = email

    try:
        checkout_session = stripe.checkout.Session.create(
            mode="subscription",
            payment_method_types=["card"],
            line_items=[
                {
                    "price": tier.stripe_price_id,
                    "quantity": 1,
                }
            ],
            success_url=f"{settings.STRIPE_SUCCESS_URL}?session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=settings.STRIPE_CANCEL_URL,
            metadata={
                "user_id": request.user.id,
                "tier_slug": tier.slug,
            },
            **customer_kwargs,
        )
    except Exception as e:
        print("Stripe error while creating Checkout Session:", repr(e))
        return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse(
        {
            "sessionId": checkout_session["id"],
            "publicKey": settings.STRIPE_PUBLISHABLE_KEY,
        }
    )


class MembershipSuccessView(TemplateView):
    template_name = "club/membership_success.html"

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get("session_id")
        membership = None

        if request.user.is_authenticated and session_id:
            try:
                stripe.api_key = settings.STRIPE_SECRET_KEY
                session = stripe.checkout.Session.retrieve(
                    session_id,
                    expand=["subscription"],
                )
                tier_slug = session.metadata.get("tier_slug")
                subscription = session.subscription  # may be an object if expanded

                tier = MembershipTier.objects.get(slug=tier_slug)
                membership, created = Membership.objects.get_or_create(
                    user=request.user,
                    defaults={
                        "tier": tier,
                        "stripe_subscription_id": getattr(subscription, "id", None) or session.get("subscription"),
                        "active": True,
                    },
                )
                if not created:
                    membership.tier = tier
                    membership.stripe_subscription_id = getattr(subscription, "id", None) or session.get("subscription")
                    membership.active = True
                    membership.save()
            except Exception:
                # swallow errors for now – still show success page
                membership = None

        context = self.get_context_data(**kwargs)
        context["membership"] = membership
        return self.render_to_response(context)


class MembershipCancelView(TemplateView):
    template_name = "club/membership_cancel.html"


