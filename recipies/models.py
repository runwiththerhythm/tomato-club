from django.db import models
from django.utils.text import slugify


class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("advanced", "Advanced"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    intro = models.TextField(
        help_text="Short, 1–3 sentence introduction to the recipe."
    )
    ingredients = models.TextField(
        help_text="List ingredients, one per line."
    )
    instructions = models.TextField(
        help_text="Step-by-step method. Use blank lines to separate steps."
    )

    prep_time_minutes = models.PositiveIntegerField(
        null=True, blank=True, help_text="Prep time in minutes"
    )
    cook_time_minutes = models.PositiveIntegerField(
        null=True, blank=True, help_text="Cooking time in minutes"
    )
    serves = models.PositiveIntegerField(
        null=True, blank=True, help_text="How many people this serves"
    )
    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default="easy",
    )
    is_freezer_friendly = models.BooleanField(default=False)
    is_good_for_gluts = models.BooleanField(
        default=False,
        help_text="Tick if this is especially good for using up a glut of tomatoes.",
    )

    image = models.ImageField(
        upload_to="recipes/",
        blank=True,
        null=True,
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    @property
    def total_time_minutes(self):
        return (self.prep_time_minutes or 0) + (self.cook_time_minutes or 0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
