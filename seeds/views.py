from django.views.generic import ListView, DetailView
from .models import TomatoVariety


class TomatoVarietyListView(ListView):
    model = TomatoVariety
    template_name = "seeds/variety_list.html"
    context_object_name = "varieties"
    paginate_by = 12

    def get_queryset(self):
        # Only show active varieties
        return (
            TomatoVariety.objects.filter(is_active=True)
            .order_by("name")
        )


class TomatoVarietyDetailView(DetailView):
    model = TomatoVariety
    template_name = "seeds/variety_detail.html"
    context_object_name = "variety"
