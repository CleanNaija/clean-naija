import os 
from urllib.parse import urlparse 


# Get the DATABASE_URL from environment variables
DATABASE_URL = os.getenv('DATABASE_URL', 'postgres://admin:admin@db:5432/waste_management')

# Parse the DATABASE_URL to break it into its components
url = urlparse(DATABASE_URL)


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-313i_hb54+siqmh$z)y#avxmrim(_*0s3$o$g63yrg@sh=fjj4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'waste',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'drf_yasg',
]

# settings.py

AUTH_USER_MODEL = 'waste.CustomUser'



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'waste_management',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'db',  # Matches the service name in your docker-compose.yml
        'PORT': '5432',
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8},  # Set minimum length
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

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # Use JWT Authentication
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Default to requiring authenticated users
    ],
     'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '5/minute',  # Allow 5 requests per minute per user
    },
}
from datetime import datetime,timedelta

# JWT Configuration (Optional)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),  # Token expires after 30 minutes
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # Refresh token lifetime (1 day)
    'ROTATE_REFRESH_TOKENS': False,  # Do not rotate refresh tokens
    'BLACKLIST_AFTER_ROTATION': True,  # Blacklist tokens after they are rotated
    'AUTH_HEADER_TYPES': ('Bearer',),  # Use 'Bearer' for Authorization header
}


""""
Implemented these 
Email Verification – To ensure valid email addresses during registration.
Password Strength Policy – To enforce strong passwords for better security.
2FA (Two-Factor Authentication) – Adds an extra layer of security.
Role-based Permissions – To manage access levels based on roles.
API Rate Limiting – To protect your API from excessive requests.
API Documentation – To provide a self-explanatory API interface.
User Activity Logging – To track actions for security and audit purposes.
Data Encryption – For securing sensitive data.
Session Management – To manage user sessions effectively, including token invalidation.
Frontend Authentication Flow – Ensure proper integration between the frontend and backend for seamless user management.
"""