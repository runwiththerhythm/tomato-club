from django.urls import path
from .views import home, MembershipView, AboutView, JoinView, ContactView, ResourcesView, newsletter_signup

app_name = "club"

urlpatterns = [
    path("", home, name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("membership/", MembershipView.as_view(), name="membership"),
    path("join/", JoinView.as_view(), name="join"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("resources/", ResourcesView.as_view(), name="resources"),
    path("newsletter/signup/", newsletter_signup, name="newsletter_signup"),
]
