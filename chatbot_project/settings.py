"""
Django settings for chatbot_project project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
# from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent  #-----> Without static option
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSRF_TRUSTED_ORIGINS= ["https://web-production-4bebf.up.railway.app"]


# Session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Using database-backed sessions




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'django-insecure-14-gmxg$!9tne$7e#6c)bq3!wes8!*jr6gv6e6j!(fyi$if^9)'


# load_dotenv()
# SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret_key')
# DEBUG = os.getenv('DEBUG', 'False') == 'True'



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False



# ALLOWED_HOSTS = []

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chatbot',
]

# Session timeout settings
SESSION_COOKIE_AGE = 300  # 30 minutes
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Expire session when browser is closed
SESSION_SAVE_EVERY_REQUEST = True  # Refresh session timeout on each request

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # ---------> For Deployment 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chatbot_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], #------> For java script and css  
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

WSGI_APPLICATION = 'chatbot_project.wsgi.application'  #-----> Correct



# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',     # -----> chages from ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db. sqlite3
        'NAME': BASE_DIR / 'db.sqlite3',            # -----> chages from ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db. sqlite3
        
        # ---->>>>    Without environment variables
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'chatbot_db',  # Replace with your DB name
        # 'USER': 'admin',       # Replace with your username
        # 'PASSWORD': 'password123',  # Replace with your password
        # 'HOST': 'localhost',   # For Railway, you'll update this
        # 'PORT': '5432',        # Default PostgreSQL port
        # ---->>>>    Without environment variables

        # ---->>>>    With environment variables

        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': os.getenv('DB_NAME', 'chatbot_db'),
        # 'USER': os.getenv('DB_USER', 'admin'),
        # 'PASSWORD': os.getenv('DB_PASSWORD', 'password123'),
        # 'HOST': os.getenv('DB_HOST', 'localhost'),
        # 'PORT': os.getenv('DB_PORT', '5432'),
        # ---->>>>    With environment variables
    
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




STATIC_URL = '/static/'
# STATIC_ROOT = 'staticfiles'  # Directory where static files will be collected

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'chatbot/static'),  # Custom static files at the project level
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  



STATICSTORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
