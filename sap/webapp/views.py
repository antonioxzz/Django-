from django.shortcuts import render
from django.http import HttpResponse

from people.models import People


# Create your views here.
def welcome(request):
    people_number = People.objects.count()
    #people = People.objects.all()
    people = People.objects.order_by('id')
    return render(request, 'welcome.html', {'people_number':people_number, 'people': people})

