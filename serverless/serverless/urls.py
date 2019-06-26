from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("survey.urls")),
    path("glacier/", include("glacier.urls")),
    path("storage_management/", include("storage_management.urls"), name="Storage management")
]
