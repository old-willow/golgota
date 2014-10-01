"""
Django settings for golgota project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

#from django.utils.translation import ugettext as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# for gmail
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'some.email.name@some.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587

# I added.
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'home',
    'events',
    'gallery',
    'medias',
    'contact',
    'links',
)
# Possible options:
#SESSION_ENGINE = django.contrib.sessions.backends.file'
#SESSION_ENGINE = django.contrib.sessions.backends.cache'
#SESSION_ENGINE = django.contrib.sessions.backends.cache_db'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'


#SESSION_COOKIE_HTTPONLY = True

#FILE_UPLOAD_HANDLERS = (
#    'django.core.files.uploadhandler.MemoryFileUploadHandler',
#    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
#)

ROOT_URLCONF = 'golgota.urls'

WSGI_APPLICATION = 'golgota.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'golgota-db.sqlite3'),
    }
}

# Serialization
FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'home', 'fixtures'),
    os.path.join(BASE_DIR, 'events', 'fixtures'),
    os.path.join(BASE_DIR, 'gallery', 'fixtures'),
    os.path.join(BASE_DIR, 'medias', 'fixtures'),
    os.path.join(BASE_DIR, 'contact', 'fixtures'),
    os.path.join(BASE_DIR, 'links', 'fixtures'),
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

# Django documentation suggests this dummy function. Have no idea why...
ugettext = lambda s: s

# Default language that Django will use.
#LANGUAGE_CODE = 'en'
#LANGUAGE_CODE = 'hu'
LANGUAGE_CODE = 'sr-latn'

# The list of available language translations.
LANGUAGES = (
    ('sr-latn', ugettext('Serbian Latin')),
    ('hu', ugettext('Hungarian')),
    ('en', ugettext('English')),
)

LANGUAGE_COOKIE_NAME = 'django_language'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'home', 'locale'),
    os.path.join(BASE_DIR, 'events', 'locale'),
    os.path.join(BASE_DIR, 'gallery', 'locale'),
    os.path.join(BASE_DIR, 'medias', 'locale'),
    os.path.join(BASE_DIR, 'contact', 'locale'),
    os.path.join(BASE_DIR, 'links', 'locale'),
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',  # is this needed?
)

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Belgrade'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Should STATIC_ROOT be defined only when out of DEBUG mode?
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Adding path to common static file assets.
if DEBUG:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
