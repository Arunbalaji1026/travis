from django.contrib import admin
from django.urls import path
from rest_framework.views import APIView
from .views import *
from .serializers import *

urlpatterns = [
    path('geo/search/params',indexList.as_view(),name ="indexList"),
]
