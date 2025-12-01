# club/models.py
from django.db import models
from django.conf import settings


class MembershipTier(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    price_per_year = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    short_tagline = models.CharField(max_length=255, blank=True)
    feature_list = models.TextField(
        blank=True,
        help_text="One feature per line; render as a list in the template."
    )

    # NEW: connect to Stripe
    stripe_price_id = models.CharField(
        max_length=255,
        blank=True,
        help_text="Stripe Price ID for this tier (price_xxx). Leave blank for free tiers.",
    )

    class Meta:
        ordering = ["sort_order", "price_per_year"]

    def __str__(self):
        return self.name
#Now we also add a Membership model to link a user to a tier.


class Membership(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="membership",
    )
    tier = models.ForeignKey(
        MembershipTier,
        on_delete=models.PROTECT,
        related_name="members",
    )
    stripe_subscription_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Stripe subscription ID (sub_...).",
    )
    active = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} – {self.tier.name} ({'active' if self.active else 'inactive'})"



class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_joined"]

    def __str__(self):
        return self.email