"""
Django settings for danpalmer project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not 'PRODUCTION' in os.environ

if DEBUG:
    SECRET_KEY = 'EZz8E3gPsrHnFgpBVB1rCfx1YKwgP1nuR8iyE3ETHcmfiCnNrhD34hS0'
else:
    SECRET_KEY = os.environ['SECRET_KEY']

if DEBUG:
    SITE_URL = 'http://localhost:8000'
else:
    SITE_URL = 'http://danpalmer.me'

TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

ALLOWED_HOSTS = (
    'danpalmer.apps.danpalmer.me',
    'www.danpalmer.me',
    'danpalmer.me',
)

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'markdown_deux',
    'whitenoise.runserver_nostatic',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrap3',
    'django_s3_storage',

    'django_google_charts',

    'danpalmer.home',
    'danpalmer.blog',
    'danpalmer.projects',
    'danpalmer.projects.complexify',
)

if not DEBUG:
    INSTALLED_APPS = INSTALLED_APPS + (
        'raven.contrib.django.raven_compat',
    )

MIDDLEWARE_CLASSES = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'danpalmer.core.context_processors.settings_context',
)

if DEBUG:
    TEMPLATE_CONTEXT_PROCESSORS += (
        'django.core.context_processors.debug',
    )

ROOT_URLCONF = 'danpalmer.urls'

WSGI_APPLICATION = 'danpalmer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('DATABASE_HOST', ''),
        'PORT': 5432,
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'storage')

COPYRIGHT = 'Copyright (c) %d, Dan Palmer' % datetime.date.today().year

MARKDOWN_DEUX_STYLES = {
    'trusted': {
        'extras': {
            'html-classes': {'table': 'table'},
            'code-friendly': None,
            'fenced-code-blocks': True,
            'tables': True,
        },
        # Warning, do not use for publicly generated content.
        'safe_mode': False,
    },
}

MARKDOWN_DEUX_STYLES['default'] = MARKDOWN_DEUX_STYLES['trusted']

if not DEBUG:
    RAVEN_CONFIG = {'dsn': os.environ.get('SENTRY_DSN')}

if not DEBUG:
    DEFAULT_FILE_STORAGE = 'danpalmer.core.storage.PublicS3Storage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME')
AWS_REGION = 'eu-west-1'
