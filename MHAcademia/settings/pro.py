from .base import *
import os

DEBUG = False

ADMINS = {
    ('Daniel Sam', 'daniellevilucas@gmail.com')
}

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'MHAcademia',
        'USER': 'postgres',
        'PASSWORD': os.environ['POSTGRES_PASSWORD']
    }
}
