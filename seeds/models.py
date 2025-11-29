from django.db import models
from django.urls import reverse


class TomatoVariety(models.Model):
    GROWTH_HABIT_CHOICES = [
        ("indeterminate", "Indeterminate (cordon)"),
        ("determinate", "Determinate (bush)"),
        ("dwarf", "Dwarf / compact"),
    ]

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=220, unique=True, help_text="Used in the URL.")
    origin = models.CharField(
        max_length=200,
        blank=True,
        help_text="Where this variety comes from (region, breeder, family, etc.).",
    )
    growth_habit = models.CharField(
        max_length=20,
        choices=GROWTH_HABIT_CHOICES,
        blank=True,
    )
    days_to_maturity = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        help_text="Approximate days from transplant to ripe fruit (if known).",
    )
    fruit_color = models.CharField(
        max_length=100,
        blank=True,
        help_text="E.g. red, pink, yellow, striped, black, etc.",
    )
    description = models.TextField(
        blank=True,
        help_text="Short description, flavour notes, and any heritage story.",
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Use to highlight certain varieties on the homepage later.",
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Uncheck if this variety is retired or not currently available.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Tomato variety"
        verbose_name_plural = "Tomato varieties"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("seeds:variety_detail", kwargs={"slug": self.slug})
