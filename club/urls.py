from django.urls import path
from .views import home, MembershipView, AboutView, JoinView, ContactView, ResourcesView, newsletter_signup
from . import views


app_name = "club"

urlpatterns = [
    path("", home, name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("membership/", MembershipView.as_view(), name="membership"),
    path("join/", JoinView.as_view(), name="join"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("resources/", ResourcesView.as_view(), name="resources"),
    path("newsletter/signup/", newsletter_signup, name="newsletter_signup"),

     # Stripe membership endpoints
    path(
        "membership/checkout/<slug:slug>/",
        views.create_membership_checkout_session,
        name="membership_checkout",
    ),
    path(
        "membership/success/",
        views.MembershipSuccessView.as_view(),
        name="membership_success",
    ),
    path(
        "membership/cancel/",
        views.MembershipCancelView.as_view(),
        name="membership_cancel",
    ),

]
