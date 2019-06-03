from .base import *


DEBUG = True

# -----------------------------------------------------------------------------
# Databases
# -----------------------------------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "travis_ci_db",
        "USER": "travis",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
    }
}
