from django.urls import include, path
from rest_framework import routers

from .views import *

urlpatterns = [
    path('pereval/create', PerevalCreateView.as_view()),
    path('all/', PerevalListView.as_view()),
    path('pereval/detail/<int:pk>/', PerevalDetailView.as_view()),
]