from pathlib import Path
import os

# Auth user
AUTH_USER_MODEL = 'user.User'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# login URL
LOGIN_URL = '/user/login'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-j95+atc5%&o%f$#68lz6zr4eq_p4#183(r2x(815b8_hc66rq*"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "blog",
    "user",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django_extensions',
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

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "app.wsgi.application"


# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation

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

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

"""
개발 단계에서 사용하는 정적 파일이 위치한 경로들을 지정
튜플 배치 순서 대로 정적 파일을 탐색 우선순위로 작용
"""
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

"""
문자열은 반드시 /로 끝나야 한다. 
findstatic 명령어로 탐색되는 정적 파일 경로에 
STATIC_URL 경로를 합치면 실제 웹에서 접근 가능한 URL이 된다.
http://127.0.0.1:8000/static/images/logo-fff.png
"""
STATIC_URL = '/static/'

"""
collectstatic 명령어로 
Django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아넣는 경로
DEBUG가 True로 설정되어 있으면 STATIC_ROOT 설정은 작용하지 않는다.
STATIC_ROOT 경로는 STATICFILES_DIRS 등록된 경로와 같은 경로가 있어서는 안 된다.
"""
# STATIC_ROOT -> 프로젝트 완성 후 작업


# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
