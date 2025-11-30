from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "difficulty", "serves", "is_freezer_friendly", "created")
    list_filter = ("difficulty", "is_freezer_friendly", "is_good_for_gluts", "created")
    search_fields = ("title", "intro", "ingredients", "instructions")
    prepopulated_fields = {"slug": ("title",)}
