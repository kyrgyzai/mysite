from django.db import models
from datetime import datetime, timezone, timedelta

class Question(models.Model):
    question_text = models.CharField(max_length=128)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self):
        time = datetime.now(timezone.utc)
        return (time - timedelta(days=1) <= self.pub_date <= time) 

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=128)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text