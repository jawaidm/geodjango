import os
from django.contrib.gis.utils import LayerMapping
from .models import AustralianStates, AustraliaState

# Auto-generated `LayerMapping` dictionary for AustralianStates model
australia_state_mapping = {
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

aus_state_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/igismap', 'Australia_Polygon.shp'),
)

def run1(verbose=True):
    lm = LayerMapping(AustraliaState, aus_state_shp, australia_state_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


# Auto-generated `LayerMapping` dictionary for AustralianStates model
australian_states_mapping = {
    'name': 'NAME',
    'area': 'AREA',
    'totpop_cy': 'TOTPOP_CY',
    'iso_sub': 'ISO_SUB',
    'geom': 'MULTIPOLYGON',
}

aus_states_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/aus_states', 'States Map.shp'),
)

def run2(verbose=True):
    lm = LayerMapping(AustralianStates, aus_states_shp, australian_states_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

