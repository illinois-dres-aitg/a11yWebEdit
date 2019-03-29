"""
Django settings for WebEdit project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os, json
from os.path import join, abspath, dirname
from django.urls import reverse
from djangocodemirror.settings import *
from djangocodemirror.helper import codemirror_settings_update

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

here = lambda *dirs: join(abspath(dirname(__file__)), *dirs)
root = lambda *dirs: join(abspath(here("","..")), *dirs)

BASE_DIR = here("", "")
print("BASE_DIR: " + BASE_DIR)

APP_DIR  = root("")
print(" APP_DIR: " + APP_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

with open(join(BASE_DIR,'secrets.json')) as s:
	secrets = json.loads(s.read())

def get_secret(setting, secrets=secrets):
	try:
		return secrets[setting]
	except KeyError:
		error_msg = 'Set the {0} environment variable'.format(setting)
		raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_secret('DEBUG')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_secret('DEBUG')

EMAIL_HOST               = get_secret('EMAIL_HOST')

EMAIL_PORT               = get_secret('EMAIL_PORT')
EMAIL_USE_TLS            = get_secret('EMAIL_USE_TLS')

EMAIL_HOST_USER          = get_secret('EMAIL_HOST_USER')
EMAIL_HOST_USER_PASSWORD = get_secret('EMAIL_HOST_USER_PASSWORD')

DEFAULT_FROM_EMAIL       = get_secret('EMAIL_HOST_USER')
SERVER_EMAIL             = get_secret('EMAIL_HOST_USER')

if get_secret('SITE_URL').find('127.0.0.1') >= 0 or get_secret('SITE_URL').find('localhost') >= 0:
  EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ACCOUNT_ACTIVATION_DAYS = get_secret('ACCOUNT_ACTIVATION_DAYS')
REGISTRATION_EMAIL_HTML = False

ALLOWED_HOSTS = get_secret('ALLOWED_HOSTS')

ADMIN_USERNAME   = get_secret('ADMIN_USERNAME')
ADMIN_PASSWORD   = get_secret('ADMIN_PASSWORD')
ADMIN_FIRST_NAME = get_secret('ADMIN_FIRST_NAME')
ADMIN_LAST_NAME  = get_secret('ADMIN_LAST_NAME')
ADMIN_EMAIL      = get_secret('ADMIN_EMAIL')

ALLOWED_HOSTS = get_secret('ALLOWED_HOSTS');

SITE_ID       = 1
SITE_NAME     = get_secret('SITE_NAME')
SITE_URL      = get_secret('SITE_URL')
SHIB_URL      = get_secret('SHIB_URL')

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login'

# Allow django-bootstrap3 to use jquery
BOOTSTRAP3 = {
    'include_jquery': True,
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'bootstrap3',
    'pages.apps.PagesConfig',
    'accounts.apps.AccountsConfig',
    'djangocodemirror',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'WebEdit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(BASE_DIR,'templates/')],
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

WSGI_APPLICATION = 'WebEdit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':   get_secret('DATABASE_ENGINE'),
        'NAME':     get_secret('DATABASE_NAME'),
		'USER':     get_secret('DATABASE_USER'),
		'PASSWORD': get_secret('DATABASE_PASSWORD'),
		'HOST':     get_secret('DATABASE_HOST'),
		'PORT':     get_secret('DATABASE_PORT')
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'static/')

print('STATIC_ROOT: ' + STATIC_ROOT)

STATICFILES_DIRS = (
  join(APP_DIR, 'static'),
)

CODEMIRROR_SETTINGS = codemirror_settings_update(CODEMIRROR_SETTINGS, {
    'lineNumbers': True
})
