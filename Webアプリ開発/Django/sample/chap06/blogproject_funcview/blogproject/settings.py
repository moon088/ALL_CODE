"""
Django settings for blogproject project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6q6qdgpye0=bzw#$9h9a=0dtyxjcoo^zi*ao0+ejz3jqdqhq%a'

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
    # blogappを追加する
    'blogapp.apps.BlogappConfig',
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

ROOT_URLCONF = 'blogproject.urls'

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

WSGI_APPLICATION = 'blogproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

# 使用言語を設定
LANGUAGE_CODE = 'ja'

# タイムゾーンを設定
TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# constantsをインポート
from django.contrib.messages import constants
# レベル定数を指定するための環境変数MESSAGE_TAGS
MESSAGE_TAGS = {
  constants.SUCCESS: 'alert alert-success',
  }

# フォームの送信データをターミナルに出力
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# メールサーバーへの接続設定は、EMAIL_BACKENDをコメントアウトし、
# 以下のコードのコメントアウトを解除してください
# Gmailのアドレス、Gmailのアプリ用パスワードはお使いのものを入力してください

# DEFAULT_FROM_EMAIL = 'xxxxxx@gmail.com'  # メールの送信元のアドレスを入力
# EMAIL_HOST = 'smtp.gmail.com'            # GmailのSMPTサーバー　　　
# EMAIL_PORT = 587                         # SMPTサーバーのポート番号
# EMAIL_HOST_USER = 'xxxxxx@gmail.com'     # Gmailのアドレスを入力
# EMAIL_HOST_PASSWORD = 'xxxxxxxxxxxxxxxx' # Gmailのアプリ用パスワードを入力
# EMAIL_USE_TLS = True # SMTP サーバと通信する際に TLS (セキュア) 接続を使う