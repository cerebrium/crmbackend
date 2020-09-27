import os
import pytz
os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'asdkmfalskdmflaksdqwqmwe123mdklsm534kmwmpweom'

# SECURITY WARNING: don't run with debug turned on in production! ok! <--
DEBUG = False

ALLOWED_HOSTS = [
    'https://pythonicbackend.herokuapp.com',
    'pythonicbackend.herokuapp.com',
]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pythonicbackend.api',
    'rest_framework',
    'djmoney',
    'rest_auth',
    'rest_framework.authtoken',
    'django.contrib.postgres.fields',
    'corsheaders',
    'import_export',
    'django_extensions'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ORIGIN_WHITELIST = [
    "https://master.d2i61z5fsjun86.amplifyapp.com",
    "http://localhost:3000",
]

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'DELETE'
]

ROOT_URLCONF = 'pythonicbackend.urls'

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

WSGI_APPLICATION = 'pythonicbackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
  
# Nikitch Local Database Configuration
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'crmbackend',
#         'USER': 'postgres',
#         'PASSWORD': 'Ginishka04121995',
#         'HOST': 'localhost',
#         'PORT': '5432'
#     }
# }

# Ginishka local database Configuration
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'test0',
#         'USER': 'ginovevailieva',
#         'PASSWORD': 'Ginishka95',                                              
#         'HOST': 'localhost',
#         'PORT': '5432'
#     }
# }


# Deployment Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10000,
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = False

TIME_INPUT_FORMATS = '%I:%M %p'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

# Heroku: Update database configuration from $DATABASE_URL. 
import dj_database_url 
db_from_env = dj_database_url.config(conn_max_age=500) 
DATABASES['default'].update(db_from_env)