from django.contrib import admin
from django.contrib.gis import admin as gisadmin
from .models import AustraliaState, AustralianStates

#admin.site.register(AustraliaState, gisadmin.GeoModelAdmin)
#admin.site.register(AustralianStates, gisadmin.GeoModelAdmin)

@admin.register(AustraliaState)
class AustraliaStateAdmin(gisadmin.OSMGeoAdmin):
    list_display = ('name',)

@admin.register(AustralianStates)
class AustralianStatesAdmin(gisadmin.OSMGeoAdmin):
    list_display = ('name',)

