from django.conf import settings
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


class GrowDiaryEntry(models.Model):
    STAGE_CHOICES = [
        ("sown", "Sown"),
        ("germinated", "Germinated"),
        ("potted_on", "Potted on"),
        ("outdoors", "Planted outdoors"),
        ("flowering", "Flowering"),
        ("harvest", "Harvest"),
        ("other", "Other"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="grow_diary_entries",
    )
    variety = models.ForeignKey(
        "seeds.TomatoVariety",
        on_delete=models.CASCADE,
        related_name="grow_diary_entries",
    )
    date = models.DateField(default=timezone.now)
    stage = models.CharField(max_length=50, choices=STAGE_CHOICES)
    title = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    photo = CloudinaryField("photo", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return self.title or f"{self.variety.name} – {self.get_stage_display()} ({self.date})"
