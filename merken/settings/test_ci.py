from .base import *


DEBUG = True
SECRET_KEY = "$9597jcpibr3w!$(y^lm+77qp()*wc^ty%ak4v!g(@1=9p!^kp"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "travis_ci_db",
        "USER": "travis",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
    }
}
