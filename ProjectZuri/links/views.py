from django.shortcuts import render
from django.utils import timezone

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Links
from .serializers import LinkSerializer

import datetime


class PostListAPI(ListAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostCreateAPI(CreateAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDetailAPI(RetrieveAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostUpdateAPI(UpdateAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDeleteAPI(DestroyAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer


class ActiveLinkView(APIView):
    """
    returns a list of all active (publicly acccessible) links
    """

    def get(self, request):
        """
        Invoked whwnever a HTTP GET Requestis made to this View
        """
        qs = Links.public.all()
        data = LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class RecentLinkView(APIView):
    """"Returns a list of recently created active links"""

    def get(self, request):
        """Invoked when a HTTP GET request is made to this view"""
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = Links.public.filter(created_date=seven_days_ago)
        data = LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
