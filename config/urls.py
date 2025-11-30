from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("seeds/", include("seeds.urls")),
    path("profile/", include("profiles.urls")),

    # Main site (club) - namespaced
    path("", include(("club.urls", "club"), namespace="club")),
    path("recipes/", include("recipes.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
