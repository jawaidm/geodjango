from django.db import models
from django.contrib.gis.db import models as gismodels


#class WeatherStation(gismodels.Model):
#
#    wmoid = models.IntegerField(primary_key=True)
#    name = models.CharField(max_length=256)
#
#    geom = gismodels.PointField()
#
#    objects = gismodels.GeoManager()
#
#    def __str__(self):
#        return self.name


class AustraliaState(gismodels.Model):
    id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    enname = models.CharField(max_length=254)
    locname = models.CharField(max_length=254)
    offname = models.CharField(max_length=254, null=True)
    boundary = models.CharField(max_length=254)
    adminlevel = models.IntegerField()
    wikidata = models.CharField(max_length=254)
    wikimedia = models.CharField(max_length=254)
    timestamp = models.CharField(max_length=254)
    note = models.CharField(max_length=254, null=True)
    path = models.CharField(max_length=254)
    rpath = models.CharField(max_length=254)
    iso3166_2 = models.CharField(max_length=254, null=True)
    geom = gismodels.MultiPolygonField(srid=4326)

    objects = models.Manager()

    def __str__(self):
        return self.name

class AustralianStates(models.Model):
    name = models.CharField(max_length=70, null=True)
    area = models.FloatField(null=True)
    totpop_cy = models.BigIntegerField(null=True)
    iso_sub = models.CharField(max_length=5, null=True)
    geom = gismodels.MultiPolygonField(srid=4326)

    objects = models.Manager()

    def __str__(self):
        return self.name



