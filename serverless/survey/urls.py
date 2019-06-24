from django.urls import include, path
from rest_framework import routers
from survey import views

router = routers.DefaultRouter()
router.register(r'survey', views.SurveyViewSet, base_name="survey")
router.register(r"question", views.QuestionViewSet, base_name="question")
router.register(r"selection", views.SelectionViewSet, base_name="selection")
# router.register(r"avg/survey", views.GetAvgTimePerSurvey, base_name="avg_survey"
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
