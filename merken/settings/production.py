import sentry_sdk
from decouple import config
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

sentry_dsn = config("SENTRY_DSN")
sentry_sdk.init(
    dsn=sentry_dsn,
    integrations=[DjangoIntegration()]
)

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
