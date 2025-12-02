from django.contrib import admin
from .models import GrowDiaryEntry


@admin.register(GrowDiaryEntry)
class GrowDiaryEntryAdmin(admin.ModelAdmin):
    list_display = ("user", "variety", "stage", "date", "created_at")
    list_filter = ("stage", "date", "variety")
    search_fields = ("user__username", "variety__name", "notes", "title")
    raw_id_fields = ("user", "variety")
