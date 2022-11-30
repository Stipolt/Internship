from django.shortcuts import render
from rest_framework import generics
from .serializers import PerevalDetailSerializer, PerevalListSerializer
from .models import Pereval


class PerevalCreateView(generics.CreateAPIView):
    serializer_class = PerevalDetailSerializer


class PerevalListView(generics.ListAPIView):
    serializer_class = PerevalDetailSerializer
    queryset = Pereval.objects.all()


class PerevalDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PerevalDetailSerializer
    queryset = Pereval.objects.all()