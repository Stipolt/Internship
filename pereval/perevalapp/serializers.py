from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Pereval, Image, Area, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"


class PerevalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = ('id', 'title', 'user', 'coord_id')


class PerevalDetailSerializer(serializers.ModelSerializer):
    image = serializers.SlugRelatedField(slug_field="title", read_only=True,  many=True)
    area = serializers.SlugRelatedField(slug_field="title", read_only=True, many=True)
    coords = serializers.SlugRelatedField(slug_field=f'latitude.longitude height', read_only=True)

    class Meta:
        model = Pereval
        fields = '__all__'
