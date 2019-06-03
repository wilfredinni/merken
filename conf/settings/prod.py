import sentry_sdk
from decouple import config
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *


DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1"]  # ie. ["ip-address", "www.site.com"]

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------

sentry_dsn = config("SENTRY_DSN")
sentry_sdk.init(
    dsn=sentry_dsn,
    integrations=[DjangoIntegration()]
)

# -----------------------------------------------------------------------------
# Security
# -----------------------------------------------------------------------------

SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
