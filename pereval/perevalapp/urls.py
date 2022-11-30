from django.urls import include, path
from .views import *


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('pereval/create', PerevalCreateView.as_view()),
    path('all/', PerevalListView.as_view()),
    path('pereval/detail/<int:pk>/', PerevalDetailView.as_view()),
]