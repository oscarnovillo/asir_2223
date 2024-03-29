from django.utils import timezone
import datetime
from django.db import models

# Create your models here.



class Question(models.Model):
    class Meta:
        permissions = [("can_eat_pizzas", "Can eat pizzas")]
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField("date published")
    
    def __str__(self) -> str:
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.choice_text