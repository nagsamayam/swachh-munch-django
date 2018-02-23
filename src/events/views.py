from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class EventsListView(View):
    def get(self, request):
        return HttpResponse("Hai")


class EventsDetailView(View):
    def get(self, request):
        return HttpResponse("This is detials page")