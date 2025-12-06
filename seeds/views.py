# seeds/views.py
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import TomatoVariety


class TomatoVarietyListView(ListView):
    model = TomatoVariety
    template_name = "seeds/variety_list.html"
    context_object_name = "varieties"
    paginate_by = 12

    def get_queryset(self):
        # Start with active varieties only
        qs = TomatoVariety.objects.filter(is_active=True)

        request = self.request
        q = request.GET.get("q", "").strip()
        colour = request.GET.get("colour", "").strip()
        habit = request.GET.get("habit", "").strip()
        sort = request.GET.get("sort", "").strip() or "name"

        # Text search – name and origin
        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(origin__icontains=q)
            )

        # Colour filter – use icontains to work with free-text fruit_color
        if colour:
            qs = qs.filter(fruit_color__icontains=colour)

        # Growth habit filter – assuming growth_habit is a choices field
        if habit:
            qs = qs.filter(growth_habit=habit)

        # Sorting options
        if sort == "name":
            qs = qs.order_by("name")
        elif sort == "maturity_asc":
            qs = qs.order_by("days_to_maturity", "name")
        elif sort == "maturity_desc":
            qs = qs.order_by("-days_to_maturity", "name")
        elif sort == "origin":
            qs = qs.order_by("origin", "name")
        else:
            qs = qs.order_by("name")

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        request = self.request

        ctx["current_filters"] = {
            "q": request.GET.get("q", "").strip(),
            "colour": request.GET.get("colour", "").strip(),
            "habit": request.GET.get("habit", "").strip(),
            "sort": request.GET.get("sort", "").strip() or "name",
        }

        # These power the pills in the template
        ctx["colour_choices"] = [
            ("red", "Red"),
            ("orange", "Orange / Tangerine"),
            ("yellow", "Yellow"),
            ("green", "Green when ripe"),
            ("striped", "Striped / Bi-colour"),
            ("black", "Dark / Black"),
            ("pink", "Pink / Rose"),
        ]

        ctx["habit_choices"] = [
            ("cordon", "Cordon / Indeterminate"),
            ("bush", "Bush / Determinate"),
            ("dwarf", "Dwarf"),
        ]

        ctx["sort_choices"] = [
            ("name", "Name A–Z"),
            ("maturity_asc", "Earliest to latest"),
            ("maturity_desc", "Latest to earliest"),
            ("origin", "Origin (A–Z)"),
        ]

        return ctx


class TomatoVarietyDetailView(DetailView):
    model = TomatoVariety
    template_name = "seeds/variety_detail.html"
    context_object_name = "variety"
