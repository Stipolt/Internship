from django.contrib import admin
from .models import User, Pereval, Image, PerevalImage, Area, Coords, PerevalArea

# Register your models here.
admin.site.register(User)
admin.site.register(Pereval)
admin.site.register(Image)
admin.site.register(Area)
admin.site.register(Coords)
admin.site.register(PerevalArea)
admin.site.register(PerevalImage)