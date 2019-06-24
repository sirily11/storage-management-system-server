from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    title = models.CharField(max_length=1000)
    from_user = models.ForeignKey(to=User,
                                  on_delete=models.CASCADE,
                                  related_name="user",
                                  null=True,
                                  blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    survey = models.ForeignKey(to=Survey, on_delete=models.CASCADE, related_name="questions")
    multiple_choices = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Selection(models.Model):
    for_question = models.ForeignKey(
        to=Question,
        on_delete=models.CASCADE,
        related_name="selections")
    title = models.CharField(max_length=1000)
    to_question = models.ForeignKey(to=Question,
                                    on_delete=models.SET_NULL,
                                    null=True,
                                    blank=True,
                                    related_name="To")

    def __str__(self):
        return self.title


class SurveyUser(models.Model):
    take_at = models.DateTimeField(auto_now_add=True)
    survey = models.ForeignKey(to=Survey, on_delete=models.SET_NULL, null=True, blank=True)


class UserSelection(models.Model):
    user = models.ForeignKey(to=SurveyUser, on_delete=models.CASCADE)
    time_takes = models.FloatField(default=0)
    selection = models.ForeignKey(to=Selection, on_delete=models.CASCADE)
