from django.contrib import admin
from .models import MembershipTier, NewsletterSubscriber, Membership


@admin.register(MembershipTier)
class MembershipTierAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "price_per_year", "is_active", "sort_order")
    list_editable = ("price_per_year", "is_active", "sort_order")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "date_joined")
    search_fields = ("email",)


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("user", "tier", "active", "started_at")
    list_filter = ("tier", "active")
    search_fields = ("user__email", "user__username")
