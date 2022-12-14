import os
from datetime import timedelta

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(os.path.dirname(BASE_DIR), '.env')
load_dotenv(dotenv_path=env_path)

SECRET_KEY = os.getenv(
    'SECRET_KEY',
    default='ytrewq',
)

DB_ENGINE = os.getenv(
    'django.db.backends.postgresql',
    default='django.db.backends.postgresql',
)

DB_NAME = os.getenv(
    'postgres',
    default='postgres',
)

POSTGRES_USER = os.getenv(
    'postgres',
    default='postgres',
)

POSTGRES_PASSWORD = os.getenv(
    'postgres',
    default='postgres',
)

DB_HOST = os.getenv(
    'db',
    default='db',
)

DB_PORT = os.getenv(
    '5432',
    default='5432',
)

DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'reviews.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_simplejwt',
    'django_filters',
    'drf_yasg',
    'rest_framework',
    'reviews.apps.ReviewsConfig',
    'api.apps.ApiConfig',
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

ROOT_URLCONF = 'api_yamdb.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'api_yamdb.wsgi.application'


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('NAME'),
            'USER': os.getenv('USER'),
            'PASSWORD': os.getenv('PASSWORD'),
            'HOST': os.getenv('HOST'),
            'PORT': os.getenv('PORT'),
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.NumericPasswordValidator',
    },
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=3),
    'UPDATE_LAST_LOGIN': True,
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination'
    '.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'description': '???????? ???? ????????????. ???????????? ??????????: Bearer <?????? ??????????>',
            'in': 'header',
        }
    },
    'USE_SESSION_AUTH': False,
    'DEFAULT_AUTO_SCHEMA_CLASS': 'api.swagger_schemas.CustomAutoSchema',
}

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/'),)

RECIPIENTS_EMAIL = [os.getenv('RECIPIENTS_EMAIL')]
DEFAULT_FROM_EMAIL = os.getenv('RECIPIENTS_EMAIL')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

LOGGER_LINE_SEPARATOR = "-" * 80

if DEBUG is False:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'file': {
                'format': f'{LOGGER_LINE_SEPARATOR}\n'
                '{asctime} - {name} - {levelname}'
                ' - {module} - {filename} - {message}',
                'style': '{',
            }
        },
        'handlers': {
            'file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': 'logs/logger.log',
                'formatter': 'file',
                'encoding': 'UTF-8',
            }
        },
        'loggers': {
            'django.request': {
                'level': 'ERROR',
                'handlers': ['file'],
                'propagate': True,
            },
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['file'],
                'propagate': True,
            },
        },
    }
