from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Pereval, Image, Area, User, Coords


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


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = "__all__"


class PerevalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = ('id', 'title', 'user', 'coord_id')


# сделал так + во view , вместо вложенных def get/post/put  (simple is better than complex & flat is better than nested)
class PerevalDetailSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=False, many=True)
    area = AreaSerializer(read_only=False, many=True)
    coord_id = CoordSerializer(read_only=False)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Pereval
        fields = '__all__'

