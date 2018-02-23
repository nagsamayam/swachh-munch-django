from django.urls import path
from .views import ChannelListView

app_name = 'basic'
urlpatterns = [
    path('', ChannelListView.as_view(), name="create-list-channels")
]