from pathlib import Path
import cloudinary

# =============================
# Base Directory
# =============================
BASE_DIR = Path(__file__).resolve().parent.parent


# =============================
# Security
# =============================
SECRET_KEY = 'django-insecure-test-key'

DEBUG = True

ALLOWED_HOSTS = []


# =============================
# Applications
# =============================
INSTALLED_APPS = [
    # Cloudinary
    'cloudinary',
    'cloudinary_storage',

    # Django Core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'core',
    'catalog',
    'orders',
]


# =============================
# Middleware
# =============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =============================
# URLs & WSGI
# =============================
ROOT_URLCONF = 'carsapp.urls'

WSGI_APPLICATION = 'carsapp.wsgi.application'


# =============================
# Templates
# =============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / 'templates',
        ],

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


# =============================
# Database (SQLite)
# =============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =============================
# Password validation
# =============================
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


# =============================
# Language & Timezone
# =============================
LANGUAGE_CODE = 'ar'

TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True
USE_TZ = True


# =============================
# Static Files
# =============================
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'


# =============================
# Media (Cloudinary)
# =============================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # لن يُستخدم فعليًا بعد Cloudinary


# =============================
# Cloudinary Configuration
# =============================
cloudinary.config(
    cloud_name="dpgmo8dmt",
    api_key="764645471674785",
    api_secret="nLdMLcRGcM8bfV7mhmQ7GsUIqAA", 

    secure=True
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# =============================
# Default Auto Field
# =============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
