from django.shortcuts import render
from django.http import HttpResponse

from .api_util import fetch_videos
from .models import Videos
from .serializers import VideosSerializer

from rest_framework import generics, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


def fetch_new_posts(request):
    try:
        fetch_videos()
        return HttpResponse("Videos fetched successfully",status=status.HTTP_200_OK)
    except:
        return HttpResponse("Error fetching videos",status=status.HTTP_404_NOT_FOUND)


class VideoList(generics.ListAPIView):
    queryset = Videos.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
   
    # Search and filter fields
    search_fields = ['title']
    filter_fields = ['channelTitle']

    # For sorting the videos' data in reverse chronological order by default
    ordering = ['-publishingDateTime']
    serializer_class = VideosSerializer
    pagination_class = PageNumberPagination