from django.shortcuts import render, get_list_or_404
# Create your views here.
from django.http import HttpRequest, HttpResponse
#from .models import Dash_config

def index(request):

    dash = ''
    return render(request, 'AOE_dash/dash.html', {'dash': dash})
    #return HttpResponse("This is where you Explore. <br> <br> Are you curious?")
