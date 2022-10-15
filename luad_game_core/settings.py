"""
Django settings for luad_game project.
Generated by 'django-admin startproject' using Django 3.2.14.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import sys
from datetime import timedelta
from pathlib import Path

from django.utils.translation import gettext_lazy as _
import environ


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'user',
    'lottery',
    'common',
    'deposit',
    'commission',
    'instalment',
    'low_high',
    'three_disgits_prize',
    'two_disgits_prize',
    'lottery_day',
    'lottery_time',

    # The following Django contrib apps must be in TENANT_APPS
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'parler',

    'sorl.thumbnail',
    'sorl_thumbnail_serializer',

    'django_cleanup.apps.CleanupConfig',

]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = 'luad_game_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'luad_game_core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        # Tenant Engine
        'ENGINE': 'django.db.backends.postgresql',
        # set database name
        'NAME': os.getenv('DB_NAME'),
        # set your user details
        'USER': os.getenv('DB_USR'),
        'PASSWORD': os.getenv('DB_PWD'),
        'HOST': 'localhost',
        'POST': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:6006",
    "http://localhost:6007",
    "http://localhost:8000",
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=600),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=600),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)


LANGUAGES = [
    ('la', _('Lao')),
    ('en', _('English')),

]

PARLER_LANGUAGES = {
    None: (
        {'code': 'en', },
        {'code': 'la', },
    ),
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': False,   # Default
    }
}
TRANSLATE_MIXIN = 'common.translate.mixings.TranslatedSerializerMixin'
TRANSLATE_FIELD = 'common.translate.field.DRFTranslatedFieldsField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

THUMBNAIL_FORCE_OVERWRITE = True

DEPOSIT_MODEL = 'deposit.models.Deposit'
COMMISSION_MODEL = 'commission.models.Commission'
