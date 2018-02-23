from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventsListView.as_view(), name="events-list"),
    path('details/', views.EventsDetailView.as_view(), name="events-details"),
]