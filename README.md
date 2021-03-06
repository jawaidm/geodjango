## GeoDjango Tutorial

sudo apt install gdal-bin postgis


# Create DB
CREATE ROLE jawaidm WITH PASSWORD 'test123' SUPERUSER
ALTER ROLE jawaidm LOGIN;
create database geodjango;
alter role jawaidm superuser; # for postis EXTENSION
\q

psql -U jawaidm -W -h localhost -d geodjango
CREATE EXTENSION postgis;
\q

# Create virtualenv
virtualenv -p python3.6 venv
. venv/bin/activate

# Create migrations
./manage.py showmigrations
./manage.py migrate

# inspect shape file
ogrinfo world/data/TM_WORLD_BORDERS-0.3.shp
ogrinfo -so world/data/TM_WORLD_BORDERS-0.3.shp TM_WORLD_BORDERS-0.3

# inspect GeoJSON file
python manage.py ogrinspect data/example_geojson.json MyModel --srid=4326 --mapping --multi

# install GDAL
"python-gdal" version 2.1.0 requires gdal version 2.1.0 . So the install of "libgdal1" version 1.11.3 isn't sufficient. Get gdal-2.1.0 : http://download.osgeo.org/gdal/2.1.0/gdal-2.1.0.tar.gz

And the ~43 dependencies : $ sudo apt-get build-dep gdal

Building and installing gdal-2.1.0 and the Python bindings :

$ cd gdal-2.1.0/
$ ./configure --prefix=/usr/
$ make
$ sudo make install
$ cd swig/python/
$ sudo python setup.py install

# inspect WMF endpoint (from OpenLayers WFS example - works)
ogr2ogr -f GeoJSON CadastreAddress_Example1.json "https://ahocevar.com/geoserver/wfs?service=WFS&version=1.1.0&request=GetFeature&typename=osm:water_areas&outputFormat=application/json&srsname=EPSG:3857&bbox=-8936653.027920483,5370452.51819444,-8881121.5268713,5393383.626679991,EPSG:3857" OGRGeoJSON -s_srs EPSG:3857 -t_srs EPSG:4326
