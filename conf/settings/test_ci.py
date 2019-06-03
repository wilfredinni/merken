from .base import *

DEBUG = False

SECRET_KEY = env("SECRET_KEY", default="myverysecretkey")

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}
