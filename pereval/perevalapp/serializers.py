from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Pereval


class PerevalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = ('id', 'title', 'user', 'coord_id')


class PerevalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = '__all__'
