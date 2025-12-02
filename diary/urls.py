from django.urls import path
from .views import (
    GrowDiaryListView,
    GrowDiaryDetailView,
    GrowDiaryCreateView,
    GrowDiaryUpdateView,
    GrowDiaryDeleteView,
)

app_name = "diary"

urlpatterns = [
    path("", GrowDiaryListView.as_view(), name="entry_list"),
    path("add/", GrowDiaryCreateView.as_view(), name="entry_add"),
    path("<int:pk>/", GrowDiaryDetailView.as_view(), name="entry_detail"),
    path("<int:pk>/edit/", GrowDiaryUpdateView.as_view(), name="entry_edit"),
    path("<int:pk>/delete/", GrowDiaryDeleteView.as_view(), name="entry_delete"),
]
