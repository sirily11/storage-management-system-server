from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet, base_name="Category")
router.register(r'series', views.SeriesViewSet, base_name="Series"),
router.register(r'author', views.AuthorViewSet, base_name="author"),
router.register(r'location', views.LocationViewSet, base_name="location"),
router.register(r'detailposition', views.DetailPositionViewSet, base_name="detail position"),
router.register(r'itemimage', views.ItemImageViewSet, base_name="Item image")
router.register(r'item', views.ItemViewSet, base_name="Item")
router.register(r'files', views.ItemFileViewSet, base_name="files")

urlpatterns = [
    path('', include(router.urls)),
    path('settings', views.GetAllSettingsViewSet.as_view()),
    path('searchByQR', views.GetByQR.as_view())

]
