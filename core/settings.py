import os
import sys
from pathlib import Path

# 1. Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Add the 'apps' folder to the system path (Professional Way)
# This allows us to directly access 'users' instead of having to access 'apps.users' in some cases.
PROJECT_APPS_PATH = os.path.join(BASE_DIR, 'apps')
sys.path.insert(0, PROJECT_APPS_PATH)

# 3. Security (We recommend using python-dotenv in the future)
SECRET_KEY = 'django-insecure-#4231^6brm-8p%^2_f9*_m8!av2hh9=4$ok*_u@b0vzvy806ip'
DEBUG = True
ALLOWED_HOSTS = ['*']  # ปรับเป็น Domain จริงตอนขึ้น Production

# 4. Custom User Model (CORE ของ ERP)
AUTH_USER_MODEL = 'users.User'

# 5. Application Definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Core ERP Modules
    'users.apps.UsersConfig',
    'base.apps.BaseConfig',
    'inventory.apps.InventoryConfig',
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

ROOT_URLCONF = 'core.urls'

# 6. Templates Configuration (Point for resolving 404 and UI issues)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# 7. Database (Postgres SQL - Enterprise Standard)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecosystem_db',
        'USER': 'tmr_admin',
        'PASSWORD': 'ynyp2013@min',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# 8. Password Validation (ERP Strict Policy)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 9. Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Bangkok'
USE_I18N = True
USE_TZ = True

# 10. Auth Redirect Logic
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'

# 11. Static & Media Files
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Added media file management (for company logos/profile pictures)
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
