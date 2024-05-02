"""
Django settings for edu project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-6(2o^2^31fl*6+q%reso(j*^g65!$d%3^^i(*&nweg0$!tyyak"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

"""
Burada Allowed Hosts alanına wifi alanına bağlı iken ip adresini girerseniz aynı wifi ağına bağlı olan
diğer cihazlardan ip adresini yazıp sonuna :8000 eklediğiniz takdirde giriş yapabilirsiniz. 
Bu arada bunun için projeyi 'python3 manage.py runserver 0.0.0.0:8000' şeklinde çalıştırmalısınız.
"""

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "edu_app",
    "authentication",
    "drf_spectacular",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "edu.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "edu.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/



STATIC_URL = '/static/'

"""
BURADAKİ STATIC VE MEDIA AYARLARINI DJANGO MVT PROJESİNE GÖRE EKLEDİM BU PROJEYİ
DJANGO REST FRAMEWORK İLE API GELİŞTİRME FORMATINDA YAPTIĞIM İÇİN STATIC VE MEDIA AYARLARINI YORUMA ALDIM. 
MVT PROJESİNE DÖNÜŞTÜRÜLMEK İSTENİRSE KULLANILABİLİR.
"""

# STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATICFILES_DIRS = (str(BASE_DIR.joinpath("assets")),)

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


"""
Burada DRF Api Projesinin dökümantasyonunu swagger aracılığı ile sağladım. 
Settings dosyası için gerekli ayarları aşağıdaki şekildedir. 
"""

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


SPECTACULAR_SETTINGS = {
    'TITLE': 'DJANGO EDU PROJECTS',
    'DESCRIPTION': 'Matematik Röntgeni',
}