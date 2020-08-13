from rest_framework import serializers
from .models import Geo_sectors

class Geo_sectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo_sectors
        fields = '__all__'
