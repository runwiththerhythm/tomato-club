from django.test import TestCase
from django.urls import reverse

from .models import TomatoVariety


class TomatoVarietyListTests(TestCase):
    def setUp(self):
        TomatoVariety.objects.create(
            name="Ailsa Craig",
            slug="ailsa-craig",
            origin="United Kingdom",
            growth_habit="indeterminate",
            fruit_color="red",
            days_to_maturity=75,
            description="A classic red heritage tomato.",
            is_active=True,
        )
        TomatoVariety.objects.create(
            name="Yellow Pear",
            slug="yellow-pear",
            origin="Historic garden variety",
            growth_habit="indeterminate",
            fruit_color="yellow",
            days_to_maturity=75,
            description="A small yellow pear-shaped tomato.",
            is_active=True,
        )
        TomatoVariety.objects.create(
            name="Marmande",
            slug="marmande",
            origin="France",
            growth_habit="determinate",
            fruit_color="red",
            days_to_maturity=75,
            description="A classic bush tomato.",
            is_active=True,
        )
        TomatoVariety.objects.create(
            name="Retired Tomato",
            slug="retired-tomato",
            origin="Test",
            growth_habit="determinate",
            fruit_color="red",
            description="This should not appear.",
            is_active=False,
        )

    def test_seed_library_lists_active_varieties_only(self):
        response = self.client.get(reverse("seeds:variety_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ailsa Craig")
        self.assertContains(response, "Yellow Pear")
        self.assertContains(response, "Marmande")
        self.assertNotContains(response, "Retired Tomato")

    def test_seed_library_filters_by_colour(self):
        response = self.client.get(
            reverse("seeds:variety_list"),
            {"colour": "yellow"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Yellow Pear")
        self.assertNotContains(response, "Ailsa Craig")

    def test_seed_library_filters_by_growth_habit(self):
        response = self.client.get(
            reverse("seeds:variety_list"),
            {"habit": "determinate"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Marmande")
        self.assertNotContains(response, "Ailsa Craig")

    def test_seed_library_searches_by_name(self):
        response = self.client.get(
            reverse("seeds:variety_list"),
            {"q": "Ailsa"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ailsa Craig")
        self.assertNotContains(response, "Yellow Pear")

    def test_seed_library_sorts_by_maturity(self):
        response = self.client.get(
            reverse("seeds:variety_list"),
            {"sort": "maturity_asc"},
        )

        self.assertEqual(response.status_code, 200)
        varieties = list(response.context["varieties"])
        self.assertEqual(varieties[0].days_to_maturity, 75)

    def test_variety_detail_page_loads(self):
        response = self.client.get(
            reverse("seeds:variety_detail", kwargs={"slug": "ailsa-craig"})
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ailsa Craig")
        self.assertContains(response, "classic red heritage tomato")