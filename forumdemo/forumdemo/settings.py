"""
Django settings for forumdemo project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't$#vu@qg+=e3)v3_v317mcye8x^yon=ysyc6)#tvuo&m$#$sg^'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ["127.0.0.1", "112.74.98.40"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'block',
    'article.apps.ArticleConfig',
    'User',
    'activate',
    'comment',
    'message',
    'usercenter',
)
STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
        os.path.join(BASE_DIR, 'DjangoUeditor/static'),
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'middlewares.PrintParamsMiddleware',
)


ROOT_URLCONF = 'forumdemo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'forumdemo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'forumdemo',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "dist_static")

from .secret import *
LOGIN_REDIRECT_URL = "/"

import configparser
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(BASE_DIR), "conf/config.ini")
config.read(config_path)
DEBUG = config["default"].getboolean("debug")
MEDIA_URL = config["default"]["media_url"]
MEDIA_ROOT = config["default"]["media_root"]
portrait_root = config["default"]["portrait_root"]
portrait_url = config["default"]["portrait_url"]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(message)s'
        },
    },
    'handlers': {
        'info_record': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), 'log/info.log'),
            'formatter': 'verbose'
        },
        'error_record': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), 'log/error.log'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'forumdemo': {
            'handlers': ["info_record", "error_record"],
            'level': 'DEBUG',
        }
    }
}

import logging

LOGGER = logging.getLogger("forumdemo")
