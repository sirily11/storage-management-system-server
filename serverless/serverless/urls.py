from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("survey.urls")),
    path("glacier/", include("glacier.urls")),
    path("storage_management/", include("storage_management.urls"), name="Storage management")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
