from .base import *
from decouple import config

DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1"]  # ie. ["ip-address", "www.site.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USERNAME"),
        # "PASSWORD": config("DB_PASSWORD"),
        "PASSWORD": "",
        "HOST": config("DB_HOST"),
        "PORT": "",
    }
}
