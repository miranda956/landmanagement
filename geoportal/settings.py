"""
Django settings for geoportal project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('SECRET_KEY', '4ct$ragx!jn!@09061+#0lx+rgu&jyj@b6ev!i+edh2ef-f#at')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['geohub-geoportal.herokuapp.com', 'localhost']

SITE_URL = "http://localhost:8000"
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'leaflet',
    'chartit',
    'registration',
    'crispy_forms',
    'main',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

ROOT_URLCONF = 'geoportal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'geoportal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': 'dbname',
#         'USER':'user',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT':'5432',
#     }
# }





# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static","static_root")


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static","our_static"),
    # '/var/www/static/',
    )


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static","media_root")

# Django registration module settings
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window
REGISTRATION_AUTO_LOGIN = True # Automatically log the user in when they click the activation link

SITE_ID=1

#leaflet settings
LEAFLET_CONFIG = {
    # conf here
    'TILES': [
    ('OSM', 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {'attribution': '&copy; Big eye'}),
    ('Satellite', 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6IjZjNmRjNzk3ZmE2MTcwOTEwMGY0MzU3YjUzOWFmNWZhIn0.Y8bhBaUMqFiPrDRW9hieoQ', {
    'maxZoom': 18,
    'id': 'mapbox.streets-satellite'})
    ]
}
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# email settings
EMAIL_HOST_USER = "victor@mail.victorngeno.com"
EMAIL_PORT = 465
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = "Victor <{}>".format(EMAIL_HOST_USER)


ADMINS = [('Victor', EMAIL_HOST_USER)]
MANAGERS = ADMINS

# Extra local settings for db
try:
    from local_settings import DATABASES, EMAIL_HOST, EMAIL_HOST_PASSWORD
    DATABASES = DATABASES
    EMAIL_HOST = EMAIL_HOST
    EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
except ImportError:
    #means the local_settings file is not deployed online
    #production settings are defined here
    DEBUG = False
    from os import environ
    GDAL_LIBRARY_PATH = "/app/.heroku/vendor/lib/libgdal.so"
    GEOS_LIBRARY_PATH = "/app/.heroku/vendor/lib/libgeos_c.so"

    # GEOS_LIBRARY_PATH = "{}/libgeos_c.so".format(environ.get('GEOS_LIBRARY_PATH'))
    # GDAL_LIBRARY_PATH = "{}/libgdal.so".format(environ.get('GDAL_LIBRARY_PATH'))
    # PROJ4_LIBRARY_PATH = "{}/libproj.so".format(environ.get('PROJ4_LIBRARY_PATH'))


    db_from_env = dj_database_url.config()
    DATABASES = {'default': dj_database_url.config()}
    DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
