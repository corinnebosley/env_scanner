"""
This file contains lists of contents for the production environments so that
we can check against them in the tests.

The lists are copied from the source manifests in the following repository:
https://exxgitrepo:8443/projects/SSS/repos/scidesktop-environments

"""

# TODO: Add method for grabbing the source repo manifest automatically

OS40 = ['http://www-avd/conda/RedHat.x86_64/linux-64	alabaster-0.7.9-py27_0',
        'http://www-avd/conda/RedHat.x86_64/linux-64	babel-2.3.4-py27_0',
        'http://www-avd/conda/RedHat.x86_64/linux-64	biggus-0.15.0-py27_1',
        'http://www-avd/conda/RedHat.x86_64/linux-64	ca-certificates-2016.9.26-0']

for line in OS40:
    package = line.split('  ')[1]
    if package.startswith('ca-certificates'):
        name = package.split('-')[:1]
        version = line.split('-')[2]
    elif package.startswith('python-dateutils'):
        name = package.split('-')[:1]
        version = line.split('-')[2]
    else:
        name = package.split('-')[0]
        version = line.split('-')[1]


# http://www-avd/conda/RedHat.x86_64/linux-64	cartopy-0.15.0-np111py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	cf_units-1.1.3-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	configparser-3.5.0-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	curl-7.49.1-1
# http://www-avd/conda/RedHat.x86_64/linux-64	cycler-0.10.0-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	cython-0.24.1-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	docutils-0.12-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	ecmwf_grib-1.16.0-np111py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	filelock-2.0.6-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	freetype-2.6.3-1
# http://www-avd/conda/RedHat.x86_64/linux-64	functools32-3.2.3.2-py27_1
# http://www-avd/conda/RedHat.x86_64/linux-64	geos-3.4.2-4
# http://www-avd/conda/RedHat.x86_64/linux-64	h5py-2.6.0-np111py27_6
# http://www-avd/conda/RedHat.x86_64/linux-64	hdf4-4.2.12-1
# http://www-avd/conda/RedHat.x86_64/linux-64	hdf5-1.8.17-3
# http://www-avd/conda/RedHat.x86_64/linux-64	imagehash-3.1-np111py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	imagesize-0.7.1-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	iris-1.13.0-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	iris_grib-0.10.1-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	jasper-1.900.1-5
# http://www-avd/conda/RedHat.x86_64/linux-64	jinja2-2.8-py27_1
# http://www-avd/conda/RedHat.x86_64/linux-64	jpeg-9b-0
# http://www-avd/conda/RedHat.x86_64/linux-64	libmo_unpack-2.0.3-1
# http://www-avd/conda/RedHat.x86_64/linux-64	libnetcdf-4.4.1-1
# http://www-avd/conda/RedHat.x86_64/linux-64	libpng-1.6.25-1
# http://www-avd/conda/RedHat.x86_64/linux-64	libtiff-4.0.6-7
# http://www-avd/conda/RedHat.x86_64/linux-64	markupsafe-0.23-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	matplotlib-1.5.3-np111py27_1
# http://www-avd/conda/RedHat.x86_64/linux-64	metdb-0.10.0-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	metdb_rpc-4.1-0
# http://www-avd/conda/RedHat.x86_64/linux-64	mo_pack-0.2.0-np111py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	mock-1.0.1-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	monty-0.4.0-np111py27_3
# http://www-avd/conda/RedHat.x86_64/linux-64	mule-2017.08.1-np111py27_1
# http://www-avd/conda/RedHat.x86_64/linux-64	nc_time_axis-1.0.2-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	netcdf4-1.2.4-np111py27_2
# http://www-avd/conda/RedHat.x86_64/linux-64	nose-1.3.0-py27_1
# http://www-avd/conda/RedHat.x86_64/linux-64	numpy-1.11.1-py27_201
# http://www-avd/conda/RedHat.x86_64/linux-64	openssl-1.0.2h-3
# http://www-avd/conda/RedHat.x86_64/linux-64	owslib-0.10.3-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	pandas-0.20.2-np111py27_1
# http://www-avd/conda/RedHat.x86_64/linux-64	pep8-1.7.0-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	pillow-3.4.1-py27_1
# http://www-avd/conda/RedHat.x86_64/linux-64	proj.4-4.9.3-0
# http://www-avd/conda/RedHat.x86_64/linux-64	pyepsg-0.2.0-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	pygments-2.1.3-py27_1
# http://www-avd/conda/RedHat.x86_64/linux-64	pyke-1.1.1-py27_1
# http://www-avd/conda/RedHat.x86_64/linux-64	pyparsing-2.0.1-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	pyproj-1.9.5.1-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	pyro-3.16.0-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	pyshp-1.2.1-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	python-2.7.12-3
# http://www-avd/conda/RedHat.x86_64/linux-64	python-dateutil-2.5.3-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	pytz-2014.10-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	pyugrid-0.1.6-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	pywavelets-0.4.0-np111py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	requests-2.11.1-py27_1
# http://www-avd/conda/RedHat.x86_64/linux-64	scipy-0.18.1-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	setuptools-26.1.1-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	shapely-1.5.16-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	six-1.10.0-py27_1
# http://www-avd/conda/RedHat.x86_64/linux-64	snowballstemmer-1.2.1-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	sphinx-1.4.8-py27_0
# http://www-avd/conda/RedHat.x86_64/linux-64	sqlite-3.13.0-0
# http://www-avd/conda/RedHat.x86_64/linux-64	tk-8.5.19-1
# http://www-avd/conda/RedHat.x86_64/linux-64	udunits2-2.2.20-1
# http://www-avd/conda/RedHat.x86_64/linux-64	um_packing-2017.08.1-np111py27_1
# http://www-avd/conda/RedHat.x86_64/linux-64	um_utils-2017.08.1-np111py27_1
# http://www-avd/conda/RedHat.x86_64/linux-64	xz-5.2.2-0
# http://www-avd/conda/RedHat.x86_64/linux-64	zlib-1.2.8-0
#
#
# OS41 = {
#
# }
