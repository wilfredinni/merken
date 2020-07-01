from .base import *


DEBUG = False
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
SECRET_KEY = env("SECRET_KEY")

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console_format": {"format": "%(name)-12s %(levelname)-8s %(message)s"},
        "file_format": {
            "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "console_format",
        },
    },
    "loggers": {
        "django": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "apps": {"level": "DEBUG", "handlers": ["console"], "propagate": False},
    },
}

USE_SENTRY = env.bool("USE_SENTRY", default=False)

if USE_SENTRY:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(dsn=env("SENTRY_DSN"), integrations=[DjangoIntegration()])

# -----------------------------------------------------------------------------
# Security
# -----------------------------------------------------------------------------
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
