"""
Django settings for PropertyManagment project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path


from django.template.context_processors import media

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v_i5ey*-l1(2_-dzex)=ii7aqu8ro)#x2i9&+^n=hx_^&0*)n3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'PropertyApp',
    'debug_toolbar',
    'core',
    'dashbord',
    'crispy_forms',
    'crispy_bootstrap4',
    # 'drf_spectacular_sidecar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'PropertyManagment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

WSGI_APPLICATION = 'PropertyManagment.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = BASE_DIR/'static',
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
INTERNAL_IPS = [
    '127.0.0.1',  # Add your IP if running locally
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Property Management API',
    'description': 'API to manage properties, units, tenants and leases',
    'version': '1.0.0',
    # 'SERVE_INCLUDE_SCHEMA': False,
    # 'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    # 'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    # 'REDOC_DIST': 'SIDECAR',

}
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


CRISPY_TEMPLATE_PACK = 'bootstrap4'

AUTH_USER_MODEL = 'core.User'


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


LOGIN_URL = '/login/'# Redirect after logout
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10MB (default is 2.5MB)
# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # Use 465 for SSL
EMAIL_USE_TLS = True  # Set to False when using SSL
EMAIL_USE_SSL = False  # Set to True for SSL
EMAIL_HOST_USER = 'gilbertnshimyimana11@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'koupuuxnjkjphmhp'  # The app password you generated

# settings.py

STRIPE_TEST_PUBLIC_KEY = 'pk_test_51QZr9hEFxZJ4wjsIZMUSQcZDi0fLxZtwaz0yABxKofAQ8VLqR5vBwteQM0uJW3N1D8c26hTxPYZTG4S9Ac2p7QNr00EFYv8c7l'
STRIPE_TEST_SECRET_KEY = 'sk_test_51QZr9hEFxZJ4wjsIPYBe5heIaru3M8tA2s2pnhm0Dvt1fy44ctCHql1spsWCmdpbnflugbW4gww5fYieYJvP3SKH00aHsPgCl8'
