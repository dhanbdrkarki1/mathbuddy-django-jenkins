from .base import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['*']

# serving static files
STATIC_ROOT = BASE_DIR / 'static'

SECRET_KEY = config('SECRET_KEY')

# default db
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
    }
}
