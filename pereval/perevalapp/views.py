from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView

from .serializers import *
from .models import Pereval, Image, User


class UserView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ImageView(generics.ListAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class AreaView(generics.ListAPIView):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()


class PerevalDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PerevalDetailSerializer
    queryset = Pereval.objects.all()


class PerevalCreateView(generics.CreateAPIView):
    serializer_class = PerevalDetailSerializer


class PerevalListView(generics.ListAPIView):
    serializer_class = PerevalListSerializer
    queryset = Pereval.objects.all()


