from django.db import models
from categories.models import Category
from datetime import datetime

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_title = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    question_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=False)
    email_id = models.CharField(max_length=100,default='admin@gmail.com')
    answer = models.TextField(blank=True)
    
    def __str__(self):
        return self.question_title
