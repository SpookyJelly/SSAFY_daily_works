from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass


class Question(models.Model):
    question_text = models.TextField()
    def __str__(self):
        return self.question_text
    

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
    percent = models.FloatField(default=0)

    def __str__(self):
        return self.answer_text
