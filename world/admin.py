from django.contrib.gis import admin
from .models import WorldBorder

#admin.site.register(WorldBorder, admin.GeoModelAdmin)

@admin.register(WorldBorder)
class WorldBorderAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'region', 'lat', 'lon')
