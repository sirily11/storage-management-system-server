from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Survey, Question, Selection, SurveyUser, UserSelection


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "username", "email", "groups")


class SelectionSerializer(serializers.HyperlinkedModelSerializer):
    to_question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())

    class Meta:
        model = Selection
        fields = ("id", "title", "to_question")


class QuestionSerializer(serializers.ModelSerializer):
    selections = SelectionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("id", "title", "description", "image", "multiple_choices", "selections")


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ("id", "title", "created_at", "questions")


class SurveyAbstractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ("id", "title", "created_at")


class SurveyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SurveyUser
        fields = ("id", "take_at", "survey")


class UserSelectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserSelection
        fields = ("user", "time_takes", "selection")
