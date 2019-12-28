"""
Django settings for pykafe project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import django.conf.locale

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'home',
    'search',
    'contact',
    'rosetta',
    'tracking',
    'analytic',
    'leaflet',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.contrib.modeladmin',
    'wagtailcodeblock',

    'modelcluster',
    'taggit',
    'widget_tweaks',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = (
    'tracking.middleware.VisitorTrackingMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # you need this to activate language (code)
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'active_users.middleware.ActiveUsersSessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'pykafe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pykafe.context_processors.api_key',
            ],
        },
    },
]

WSGI_APPLICATION = 'pykafe.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dili'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LANGUAGES = [
    ('tet', 'Tetum'),
    ('en', 'English'),
    ('pt', 'Portugues')
]

EXTRA_LANG_INFO = dict(
    tet = {
        'bidi': False,
        'code': 'tet',
        'name': 'Tetum',
        'name_local': 'Tetum',
    },
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

django.conf.locale.LANG_INFO.update(EXTRA_LANG_INFO)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, '../node_modules'),
    os.path.join(PROJECT_DIR, 'static'),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# Javascript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/2.1/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

GEOIP_PATH =  os.path.join(BASE_DIR, 'GeoLite2_City')


# Wagtail settings

WAGTAIL_SITE_NAME = "pykafe"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://example.com'

GOOGLE_MAPS_API_KEY = "AIzaSyC7arOtQOhxhc9ozCnJ5YcuAMI_fJ5UqqA"

# tracking users
TRACK_AJAX_REQUESTS = True
TRACK_SUPERUSERS = False
TRACK_PAGEVIEWS = True
TRACK_IGNORE_STATUS_CODES = [400, 404, 403, 405, 410, 500]
TRACK_REFERER = True
TRACK_QUERY_STRING = True

mattermost = dict(
    url = "https://pykafe.pykafe.dns-cloud.net",
)

# Language of code block
WAGTAIL_CODE_BLOCK_LANGUAGES = (
    ('css', 'CSS'),
    ('html', 'HTML'),
    ('javascript', 'Javascript'),
    ('json', 'JSON'),
    ('python', 'Python'),
)


LEAFLET_CONFIG = {
    'SPATIAL_EXTENT': (124.7168, -9.7063, 127.3233, -8.1245),
    'SCALE': 'both',
}

CACHES = {
+    "default": {
+        "BACKEND": "django_redis.cache.RedisCache",
+        "LOCATION": "redis://127.0.0.1:6379/1",
+        "OPTIONS": {
+            "CLIENT_CLASS": "django_redis.client.DefaultClient",
+        }
+    }
+}
+
+ACTIVE_USERS_KEY_CLASS = 'analytic.keys.PykafeActiveUserEntry'
