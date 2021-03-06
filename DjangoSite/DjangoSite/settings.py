"""
Django settings for django_book project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k3il^m)o-6qe*&uu6pi*c(=e2s5348j^1=*x*0t$4mv06)tcq8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DjangoSite',
    'guest_book',
    'blog',
    'django_nose',
    'debug_toolbar',

)
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# NOSE_ARGS = [
#     '--with-coverage',
#     # '--cover-package=user',
#     # '--with-progressive',
#     '--verbosity=0',
#     '--with-fixture-bundling',
# ]

TEMPLATE_DIRS = (
    'D:/Works/Django/DjangoSite/templates/',
    'D:/Works/Django/DjangoSite/templates/blog',
    'D:/Works/Django/DjangoSite/templates/book',

)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)



ROOT_URLCONF = 'DjangoSite.urls'

WSGI_APPLICATION = 'DjangoSite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'NAME': 'django_site',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': '',
        'TEST_CHARSET': "utf8",
        'TEST_NAME': 'test_site',
        'TEST_ENIGNE': 'sqlite3',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
