from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'hello.html', context=None)
    #return HttpResponse("Welcome to <br> The All of Everything")