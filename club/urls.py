from django.urls import path
from .views import MembershipView

app_name = "club"

urlpatterns = [
    path("membership/", MembershipView.as_view(), name="membership"),
]
