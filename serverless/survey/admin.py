from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Survey, Question, Selection, SurveyUser, UserSelection)
class SurveyAdmin(admin.ModelAdmin):
    pass
