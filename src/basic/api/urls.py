from django.urls import path
from .views import ChannelListView, CommentIndexView

app_name = 'basic'
urlpatterns = [
    path('', ChannelListView.as_view(), name="create-list-channels"),
    path('test/', CommentIndexView.as_view(), name="create-list-comments")
]