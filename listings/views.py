from django.shortcuts import render
from listings.models import Listing
from listings.choices import categorychoices
from questions.models import Question


def index(request):
    listings = Listing.objects.all()
    questions = Question.objects.all()

    roger = {
        'questions': questions,
        'listings': listings,
        'categorychoices': categorychoices
    }
    return render(request, 'listings/listings.html', roger)

def listing(request):
    return render(request, 'listings/listing.html', roger)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')
    

    # if 'categorychoices' in request.GET:
    #     categorychoices = request.GET['categorychoices']
    #     if categorychoices:
    #         queryset_list = queryset_list.filter(categorychoices__iexact=categorychoices)
    context = {
        # 'categorychoices': categorychoices,
        'listings': queryset_list,
        
    }
    return render(request, 'listings/search.html',context)
