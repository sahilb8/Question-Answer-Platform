from django.db import models
from categories.models import Category
from datetime import datetime

class Listing(models.Model):
    listing_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    question_title = models.CharField(max_length=500)
    answer_text = models.TextField(blank=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.question_title

