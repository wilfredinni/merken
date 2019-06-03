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

# -----------------------------------------------------------------------------
# Databases
# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------
# Security
# -----------------------------------------------------------------------------

SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
