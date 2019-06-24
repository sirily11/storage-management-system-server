from django.urls import include, path
from rest_framework import routers
from glacier import views

router = routers.DefaultRouter()
router.register(r'glacier', views.GlacierViewSet, base_name="glacier")
router.register(r"vault", views.VaultViewSet, base_name="vault")
router.register(r"file", views.FileViewSet, base_name="file")

urlpatterns = [
    path('', include(router.urls)),
]
