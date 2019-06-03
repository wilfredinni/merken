import environ

env = environ.Env()
root_path = environ.Path(__file__) - 3
env.read_env(str(root_path.path(".env")))


# -----------------------------------------------------------------------------
# Basic Config
# -----------------------------------------------------------------------------

TEMPLATES = root_path('templates')
SITE_STATIC = root_path('static')
ROOT_URLCONF = "conf.urls"
WSGI_APPLICATION = "conf.wsgi.application"
SITE_ID = 1

# -----------------------------------------------------------------------------
# Time & Language
# -----------------------------------------------------------------------------

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# -----------------------------------------------------------------------------
# Security and Users
# -----------------------------------------------------------------------------

AUTH_USER_MODEL = "users.CustomUser"
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -----------------------------------------------------------------------------
# Databases
# -----------------------------------------------------------------------------

DJANGO_DATABASE_URL = env.db('DATABASE_URL')
DATABASES = {'default': DJANGO_DATABASE_URL}

# -----------------------------------------------------------------------------
# Applications configuration
# -----------------------------------------------------------------------------

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",

    # Third party
    "webpack_loader",
    "rest_framework",
    "robots",
    "cachalot",

    # Local apps
    "apps.users",
    "apps.blog",
    "apps.pages",
    "apps.core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.core.processors.global_query",
            ]
        },
    }
]

# -----------------------------------------------------------------------------
# Rest Framework
# -----------------------------------------------------------------------------

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
    ),
}

# -----------------------------------------------------------------------------
# Static & Media Files
# -----------------------------------------------------------------------------

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATICFILES_DIRS = [SITE_STATIC]
STATIC_ROOT = root_path('static_root')
MEDIA_ROOT = root_path("media_root")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dashboard/',  # must end with slash
        'STATS_FILE': root_path('dashboard/', 'webpack-stats.json'),
        'POLL_INTERVAL': 0.3,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
    }
}

# -----------------------------------------------------------------------------
# Django Debug Toolbar
# -----------------------------------------------------------------------------
