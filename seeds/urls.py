from django.urls import path
from .views import TomatoVarietyListView, TomatoVarietyDetailView

app_name = "seeds"

urlpatterns = [
    path("", TomatoVarietyListView.as_view(), name="variety_list"),
    path("<slug:slug>/", TomatoVarietyDetailView.as_view(), name="variety_detail"),
]
