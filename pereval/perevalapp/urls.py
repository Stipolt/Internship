from django.urls import include, path
from rest_framework import routers

from .views import *

urlpatterns = [
    path('submitData/create', PerevalCreateView.as_view()), # view создания
    path('submitData/', PerevalListView.as_view()),  # view всех объектов GET req
    path('submitData/<int:pk>/', PerevalDetailView.as_view()),  # view объекта GET, PATCH & PUT req
]