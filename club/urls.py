# club/urls.py
from django.urls import path
from .views import home, MembershipView, AboutView, JoinView, ContactView

app_name = "club"

urlpatterns = [
    path("", home, name="home"),
    path("membership/", MembershipView.as_view(), name="membership"),
    path("about/", AboutView.as_view(), name="about"),
    path("join/", JoinView.as_view(), name="join"),
    path("contact/", ContactView.as_view(), name="contact"),
]
