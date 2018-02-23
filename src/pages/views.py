from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    if request.method == 'GET':
        return HttpResponse("Welcome to the awesome world")