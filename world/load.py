import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder
from .models import WorldBorder

world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for AustralianStates model
australian_states_mapping = {
    'id': 'id',
    'country': 'country',
    'name': 'name',
    'enname': 'enname',
    'locname': 'locname',
    'offname': 'offname',
    'boundary': 'boundary',
    'adminlevel': 'adminlevel',
    'wikidata': 'wikidata',
    'wikimedia': 'wikimedia',
    'timestamp': 'timestamp',
    'note': 'note',
    'path': 'path',
    'rpath': 'rpath',
    'iso3166_2': 'iso3166_2',
    'geom': 'MULTIPOLYGON',
}

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'TM_WORLD_BORDERS-0.3.shp'),
)

aus_states_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Aus_States_Polygon.shp'),
)

def run(verbose=True):
    lm = LayerMapping(WorldBorder, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
