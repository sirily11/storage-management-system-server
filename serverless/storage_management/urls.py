from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet, base_name="Category")
router.register(r'series', views.SeriesViewSet, base_name="Series"),
router.register(r'author', views.AuthorViewSet, base_name="Series"),
router.register(r'location', views.LocationViewSet, base_name="Series"),
router.register(r'detail-position', views.DetailPositionViewSet, base_name="Series"),
router.register(r'item-image', views.ItemImageViewSet, base_name="Item image")
router.register(r'item', views.ItemViewSet, base_name="Item")

urlpatterns = [
    path('', include(router.urls)),
]
