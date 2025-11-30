# club/models.py
from django.db import models


class MembershipTier(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    price_per_year = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    # simple text fields for now – you can render them as bullet lists
    short_tagline = models.CharField(max_length=255, blank=True)
    feature_list = models.TextField(
        blank=True,
        help_text="One feature per line; render as a list in the template."
    )

    class Meta:
        ordering = ["sort_order", "price_per_year"]

    def __str__(self):
        return self.name


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_joined"]

    def __str__(self):
        return self.email