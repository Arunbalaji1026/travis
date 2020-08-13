from django.db import models

# Create your models here.

class Geo_sectors(models.Model):
    country_id = models.IntegerField()
    country_name = models.CharField(max_length=50, null=True)
    sector_id = models.IntegerField()
    name = models.CharField(max_length=100, null=True)
