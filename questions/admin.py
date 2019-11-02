from django.contrib import admin

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id','name','question_title','phone','question_date','email_id')
    list_display_links=('question_id','name')
    search_fields = ('name','question_title')
    list_per_page = 25  



admin.site.register(Question, QuestionAdmin)
