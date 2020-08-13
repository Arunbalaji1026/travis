from django.shortcuts import render
from .models import Geo_sectors
from .serializers import Geo_sectorsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django_filters import FilterSet
# Create your views here.

class Geo_sectorsFilter(FilterSet):
    country_id = filters.CharFilter('country_id')
    country_name = filters.CharFilter('country_name')
    class Meta:
        model = Geo_sectors
        fields = ('country_id','country_name',)


class indexList(APIView):
    def get(self, request):
        queryset = Geo_sectors.objects.all()
        serializer = Geo_sectorsSerializer(queryset, many=True)
        filter_backends = [DjangoFilterBackend]
        filter_fields = ['country_name']
        filter_class = Geo_sectorsFilter
        serializer = filter_class
        return Response(serializer.data)
