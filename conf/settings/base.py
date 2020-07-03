import os

import environ

# -----------------------------------------------------------------------------
# Basic Config
# -----------------------------------------------------------------------------
env = environ.Env()
root_path = environ.Path(__file__) - 3
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
LOGIN_REDIRECT_URL = "page_app:index"
ACCOUNT_ADAPTER = 'conf.account_adapter.NoNewUsersAccountAdapter'
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ADMIN_HONEYPOT_EMAIL_ADMINS = False

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# -----------------------------------------------------------------------------
# Databases
# -----------------------------------------------------------------------------

DJANGO_DATABASE_URL = env.db('DATABASE_URL', 'postgres://postgres@localhost:5432/pysheet2')
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
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    "rest_framework",
    "robots",
    "widget_tweaks",
    "admin_honeypot",

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
        "DIRS": [root_path('templates'), root_path('templates', 'merken')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.core.processors.global_query",
                'django.template.context_processors.request',  # allauth
            ]
        },
    }
]

# -----------------------------------------------------------------------------
# Rest Framework
# -----------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
    ),
}

# -----------------------------------------------------------------------------
# Static & Media Files
# -----------------------------------------------------------------------------
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATICFILES_DIRS = [root_path('static')]
STATIC_ROOT = root_path('static_root')
MEDIA_ROOT = root_path("media_root")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
