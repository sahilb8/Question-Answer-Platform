from django.shortcuts import render
from listings.models import Listing
from questions.models import Question


def index(request):
    listings = Listing.objects.all()
    questions = Question.objects.all()

    roger = {
        'questions': questions,
        'listings': listings,
    }
    return render(request, 'listings/listings.html', roger)

def listing(request):
    return render(request, 'listings/listing.html', roger)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')
    

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(answer_text__icontains=keywords)

    context = {
        'listings': queryset_list,
        
    }
    return render(request, 'listings/search.html',context)
