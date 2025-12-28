from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# =============================
# Security
# =============================
SECRET_KEY = 'django-insecure-nwqyd#&zx=q=ykn*l-oyithri5(+h(hg*&kfye)98c#6(k50+i'

DEBUG = True

ALLOWED_HOSTS = []


# =============================
# Applications
# =============================
INSTALLED_APPS = [
    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Project apps
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
# URLs & Templates
# =============================
ROOT_URLCONF = 'carsapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # مجلد قوالب عام
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
# WSGI
# =============================
WSGI_APPLICATION = 'carsapp.wsgi.application'


# =============================
# Database
# =============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =============================
# Password Validation
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
# Localization (Arabic + Riyadh)
# =============================
LANGUAGE_CODE = 'ar'

TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# =============================
# Static Files
# =============================
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',  # تأكد أن المجلد موجود
]


# =============================
# Default Primary Key
# =============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
