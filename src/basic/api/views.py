from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView
)
from .serializers import ChannelSerializer
from basic.models import Channel, Comment
from django.db.models import Q
from rest_framework.response import Response
from django.views.generic import View
from django.http import HttpResponse


class ChannelListView(ListCreateAPIView):
    queryset = Channel.objects.all()
    
    serializer_class = ChannelSerializer

    
    def get_queryset(self):
        qs = Channel.objects.all()
        search_keyword = self.request.GET.get('q')
        print(search_keyword)

        if search_keyword is not None:
            qs = qs.filter(
                Q(title__icontains=search_keyword) |
                Q(type__icontains=search_keyword) |
                Q(platform__icontains=search_keyword)
            ).distinct()

        return qs
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ChannelSerializer(queryset, many=True)

        return Response({"data":serializer.data})
    


class CommentIndexView(View):
    def get(self, request, *args, **kwargs):
        comments = Comment.objects.all()
        comment_list = []
        for comment in comments:
            print(comment_list.append(comment.title))
        return HttpResponse(comment_list)

        
