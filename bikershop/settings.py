"""
Django settings for bikershop project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import dj_database_url
import env
from pathlib import Path
from django.contrib.messages import constants as messages
from decouple import config
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

import cloudinary
import cloudinary_storage
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
FIXTURE_DIRS = (
   os.path.join(PROJECT_DIR, 'fixtures'),
)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
# SECRET_KEY = os.environ.get('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#DEBUG = 'DEVELOPMENT' in os.environ

#DEBUG = True if os.environ.get('DEBUG') == 'True' else False

ALLOWED_HOSTS = [os.environ.get("HEROKU_HOSTNAME"), 'localhost']
#ALLOWED_HOSTS = ['bikershopbypsz.herokuapp.com', 'localhost']
#ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = [os.environ.get("HEROKU_HOSTNAME"), '*']

# Application definition,

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'category',
    'accounts',
    'store',
    'carts',
    'orders',
    'admin_honeypot',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-info',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
]

SESSION_EXPIRE_SECONDS = 300 # 5 minutes
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_TIMEOUT_REDIRECT = 'accounts/login' 

ROOT_URLCONF = 'bikershop.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.menu_links',
                'carts.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'bikershop.wsgi.application'

AUTH_USER_MODEL = 'accounts.Account'


# Database
#https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#if 'DATABASE_URL' in os.environ:
#   DATABASES = {
#        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
#  }
#else:
#    DATABASES = {
#       'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#       }
#   }

#DATABASES = {
#    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
#
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

#STATIC_ROOT = BASE_DIR / "staticfiles"
#STATIC_URL = "static/"

# Enable WhiteNoise's GZip compression of static assets.
#STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MEDIA_URL = '/peterszabo79/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'peterszabo79')


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') #BASE_DIR #/'static'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'bikershop/static'),
)
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'






#STATIC_URL = '/static/'
#STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
#
#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CLOUDINARY_STORAGE = {
  'CLOUD_NAME' : 'peterszabo79', 
  'API_KEY' : '184378976163428', 
  'API_SECRET' : 'BY_XOmOuuwUijdXNfH9d3iqEtqI',

}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage' 


from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# SMTP configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
