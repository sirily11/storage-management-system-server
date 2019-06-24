from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from survey.serializers import UserSerializer
from .models import Survey, Question, Selection
from .serializers import SurveySerializer, QuestionSerializer, SelectionSerializer, SurveyAbstractSerializer
from rest_framework import status
from rest_framework.generics import RetrieveAPIView


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class SelectionViewSet(viewsets.ViewSet):
    def create(self, request):
        try:
            title = request.data['title']
            qid = request.data['qid']
            selection = Selection.objects.create(title=title, for_question_id=qid)
            selection.save()
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        selection = Selection.objects.get(pk=pk)
        selection.delete()
        return Response(status=status.HTTP_200_OK)

    def partial_update(self, request, pk):
        model = Selection.objects.get(pk=pk)
        serializer = SelectionSerializer(model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionViewSet(viewsets.ViewSet):
    def create(self, request):
        try:
            title = request.data['title']
            sid = request.data['sid']
            image = request.data['image']
            description = request.data['description']
            question = Question.objects.create(title=title, survey_id=sid, image=image, description=description)
            question.save()
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response(status=status.HTTP_200_OK)

    def partial_update(self, request, pk):
        model = Question.objects.get(pk=pk)
        serializer = QuestionSerializer(model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurveyViewSet(viewsets.ViewSet):

    def list(self, request, **kwargs):
        queryset = Survey.objects.all()
        serializer = SurveyAbstractSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        survey = Survey.objects.get(pk=pk)
        return Response(SurveySerializer(survey).data)

    def create(self, request):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        survey = Survey.objects.get(pk=pk)
        survey.delete()
        return Response(status=status.HTTP_200_OK)

    def partial_update(self, request, pk):
        model = Survey.objects.get(pk=pk)
        serializer = SurveySerializer(model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class GetAvgTimePerSurvey(RetrieveAPIView):
#     def get(self, request, *args, **kwargs):
#         users = Survey.objects.all().annotate()
