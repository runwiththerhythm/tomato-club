from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import Membership, MembershipTier, NewsletterSubscriber


class PublicPageTests(TestCase):
    def test_public_pages_load(self):
        url_names = [
            "club:home",
            "club:about",
            "club:join",
            "club:resources",
            "club:contact",
            "club:membership",
        ]

        for url_name in url_names:
            with self.subTest(url_name=url_name):
                response = self.client.get(reverse(url_name))
                self.assertEqual(response.status_code, 200)


class NewsletterSignupTests(TestCase):
    def test_valid_newsletter_signup_creates_subscriber_and_redirects(self):
        response = self.client.post(
            reverse("club:newsletter_signup"),
            {"email": "grower@example.com"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            NewsletterSubscriber.objects.filter(email="grower@example.com").exists()
        )

    def test_invalid_newsletter_signup_does_not_create_subscriber(self):
        response = self.client.post(
            reverse("club:newsletter_signup"),
            {"email": "not-an-email"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(NewsletterSubscriber.objects.count(), 0)


class ContactFormTests(TestCase):
    def test_contact_page_loads(self):
        response = self.client.get(reverse("club:contact"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact")

    def test_contact_form_submission_redirects(self):
        response = self.client.post(
            reverse("club:contact"),
            {
                "name": "Test Grower",
                "email": "grower@example.com",
                "subject": "Seed question",
                "message": "I would like to know more about seed saving.",
            },
        )

        self.assertEqual(response.status_code, 302)


class MembershipPageTests(TestCase):
    def setUp(self):
        self.free_tier = MembershipTier.objects.create(
            name="Free Gardener",
            slug="free-gardener",
            price_per_year=0,
            is_active=True,
            sort_order=1,
        )
        self.paid_tier = MembershipTier.objects.create(
            name="Seed Club",
            slug="seed-club",
            price_per_year=12,
            is_active=True,
            sort_order=2,
            stripe_price_id="price_test_seed_club",
        )

    def test_membership_page_loads_tiers(self):
        response = self.client.get(reverse("club:membership"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Free Gardener")
        self.assertContains(response, "Seed Club")

    def test_free_membership_link_points_to_signup(self):
        response = self.client.get(reverse("club:membership"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse("account_signup"))

    def test_logged_in_user_can_see_current_membership(self):
        user = get_user_model().objects.create_user(
            username="memberuser",
            email="member@example.com",
            password="testpass123",
        )
        Membership.objects.create(
            user=user,
            tier=self.paid_tier,
            active=True,
        )

        self.client.login(username="memberuser", password="testpass123")
        response = self.client.get(reverse("club:membership"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Seed Club")
        self.assertContains(response, "Active")


class MembershipCheckoutTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="checkoutuser",
            email="checkout@example.com",
            password="testpass123",
        )
        MembershipTier.objects.create(
            name="Seed Club",
            slug="seed-club",
            price_per_year=12,
            is_active=True,
            stripe_price_id="price_test_seed_club",
        )

    def test_checkout_requires_login(self):
        response = self.client.post(
            reverse("club:membership_checkout", kwargs={"slug": "seed-club"})
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response["Location"])

    def test_checkout_get_is_not_allowed_for_logged_in_user(self):
        self.client.login(username="checkoutuser", password="testpass123")

        response = self.client.get(
            reverse("club:membership_checkout", kwargs={"slug": "seed-club"})
        )

        self.assertEqual(response.status_code, 405)

    @override_settings(
        STRIPE_SECRET_KEY="sk_test_example",
        STRIPE_PUBLISHABLE_KEY="pk_test_example",
        STRIPE_SUCCESS_URL="https://example.com/membership/success/",
        STRIPE_CANCEL_URL="https://example.com/membership/cancel/",
    )
    @patch("club.views.stripe.checkout.Session.create")
    def test_checkout_post_returns_json_for_ajax_request(self, mock_session_create):
        mock_session_create.return_value = {
            "id": "cs_test_123",
            "url": "https://checkout.stripe.com/test-session",
        }

        self.client.login(username="checkoutuser", password="testpass123")

        response = self.client.post(
            reverse("club:membership_checkout", kwargs={"slug": "seed-club"}),
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["sessionId"], "cs_test_123")
        self.assertEqual(response.json()["publicKey"], "pk_test_example")