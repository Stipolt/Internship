from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import Pereval, Image, User


class UserView(generics.ListCreateAPIView):  # view списка и создания User, если понадобится, то add urls
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ImageView(generics.RetrieveUpdateDestroyAPIView):  # view списка и создания Image, ...
    serializer_class = ImageSerializer
    queryset = Image.objects.all()


class AreaView(generics.RetrieveUpdateDestroyAPIView):  # view списка и создания Area, ...
    queryset = Area.objects.all()


class CoordView(generics.RetrieveUpdateDestroyAPIView):  # view списка и создания Image, ...
    serializer_class = CoordSerializer
    queryset = Coords.objects.all()


class PerevalDetailView(generics.RetrieveUpdateDestroyAPIView):  # view PATCH & PUT и не только.
    serializer_class = PerevalDetailSerializer
    queryset = Pereval.objects.all()

    def get(self, request, *args, **kwargs):
        pereval = get_object_or_404(Pereval, pk=kwargs['pk'])
        serializer = PerevalDetailSerializer(pereval)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        pereval = get_object_or_404(Pereval, pk=kwargs['pk'])
        serializer = PerevalDetailSerializer(pereval, data=request.data, partial=True)
        if serializer.is_valid():
            pereval = serializer.save()
            return Response(PerevalDetailSerializer(pereval).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerevalCreateView(generics.CreateAPIView):
    serializer_class = PerevalDetailSerializer


class PerevalListView(generics.ListAPIView):
    serializer_class = PerevalListSerializer
    queryset = Pereval.objects.all()


