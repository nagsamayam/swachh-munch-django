from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
app_name = 'profiles'

urlpatterns = [
    path('', views.UserCreateView.as_view(), name='account-create')
]