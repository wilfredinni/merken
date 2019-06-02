from .base import *
from decouple import config


DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1"]

# DEVELOPMENT APPS AND MIDDLEWARES
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("DEV_DB_NAME", default="merken_db"),
        "USER": config("DEV_DB_USERNAME", default="merken_user"),
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": 5432,
    }
}

# DEBUG TOOLBAR SETTINGS
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "cachalot.panels.CachalotPanel",
    # "debug_toolbar.panels.redirects.RedirectsPanel",
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}
