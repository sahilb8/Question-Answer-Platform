from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Question
from django.core.mail import send_mail

def question(request):
    if request.method == 'POST':
        question_title = request.POST['question_title']
        name = request.POST['name']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        email_id = request.POST['email_id']
        # category_id = request.POST['category_id']

    question = Question(question_title=question_title ,name=name, phone=phone,
    user_id=user_id,category_id=9,email_id=email_id)
    

    question.save()

    #send mail
    send_mail(
        'New Question',
        name +' has asked: '+ question_title + '. Sign into admin panel for more info',
        'rdbmsproject1@gmail.com',
        [email_id],
        fail_silently=False
    )

    messages.success(request, 'Your question has been submitted')

    return redirect('dashboard')
