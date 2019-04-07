from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
#from .viewmodels import News_Index
import urllib.request
import json

# Create your views here.

def index(request):
    #News_Index();
    return HttpResponse("In today's news... everyone died <br> They're all gone")