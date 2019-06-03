from .base import *


DEBUG = False

SECRET_KEY = config("SECRET_KEY", default="$9597jcpibr3w!$(y^lm+77qp()*wc^ty%ak4v!g(@s%")

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}
