import sys
from decouple import config
from .base import *

DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1"]

# actual deployment
# ALLOWED_HOSTS = ["ip-address", "www.site.com"]

# DATABASE

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USERNAME"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": "",
    }
}

TESTING_MODE = "test" in sys.argv  # to avoid dtb to cause errors when testing
