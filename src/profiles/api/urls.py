from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
app_name = 'profiles'

urlpatterns = [
    path('', views.ProfileCreateView.as_view(), name='account-create'),
   # path('', views.ProfileCreateView.as_view(), name="profile-create")
]