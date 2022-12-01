from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Pereval, Image, Area, User, Coords


# кодим-декодим image
class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12]
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)
        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False, max_length=None, use_url=True)

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


# сделал так + во view , вместо вложенных def get/post/put  (flat is better than nested)
class PerevalDetailSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=False, many=True)
    area = AreaSerializer(read_only=False, many=True)
    coord_id = CoordSerializer(read_only=False)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Pereval
        fields = '__all__'


class PerevalCreateSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=False, many=True)
    area = AreaSerializer(read_only=False, many=True)
    coord_id = CoordSerializer(read_only=False)
    user = UserSerializer(read_only=False)

    class Meta:
        model = Pereval
        fields = '__all__'


