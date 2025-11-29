from django.contrib import admin
from .models import TomatoVariety


@admin.register(TomatoVariety)
class TomatoVarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "origin", "growth_habit", "fruit_color", "is_active", "is_featured")
    list_filter = ("growth_habit", "is_active", "is_featured", "fruit_color")
    search_fields = ("name", "origin", "description", "fruit_color")
    prepopulated_fields = {"slug": ("name",)}
