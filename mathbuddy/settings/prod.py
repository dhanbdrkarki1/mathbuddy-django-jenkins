from .base import *
from decouple import config

DEBUG = False

ALLOWED_HOSTS = ['*']

# serving static files
STATIC_ROOT = BASE_DIR / 'static'

SECRET_KEY = config('SECRET_KEY')

# default db
# DATABASES = {
#     'default': {
#     'ENGINE': 'django.db.backends.sqlite3',
#     'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

#postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config("POSTGRES_HOST"),
        'PORT': config("POSTGRES_PORT"),
    }
}