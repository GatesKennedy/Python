from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'dash.html', {'dash': dash})
    #return HttpResponse("This is where you Explore. <br> <br> Are you curious?")
