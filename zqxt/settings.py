#coding:utf-8
"""
Django settings for zqxt project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 模板中
ON_REMOTE_HOST = os.getenv('HOME') != '/Users/tu'
ON_LOCAL_HOST = not ON_REMOTE_HOST

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '.ziqiangxuetang.com', '.besttome.com', '.tuweizhong.com',
    '.yjqdjy.com', '.zqxt.org',
]

SITE_ID = 1

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&ncb%u#0n-zv33w!2h=9$$h63lf70zsj=#=$s@j&(!eqxpo5je'

# Application definition
INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.redirects',

    'tutorial',
    'tiy',
    'iclick',
    'placeholder',

    'DjangoUeditor',
    'mobi',
    'wechat_sdk.context.framework.django',
    'webshell',
    'compressor',
)

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zqxt',
        'USER': 'tu',
        'PASSWORD': 'xxx',
        'HOST': '',
        'PORT': '',
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 3600,
    }
}


MIDDLEWARE_CLASSES = (
    'zqxt.middleware.RedirectMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'mobi.middleware.MobileDetectionMiddleware',
    'zqxt.middleware.UserBasedExceptionMiddleware',
)

ROOT_URLCONF = 'zqxt.urls'

WSGI_APPLICATION = 'zqxt.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
        ],
        #'APP_DIRS': True, # choose one from APP_DIRS and loaders
        'OPTIONS': {
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.csrf',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                #'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'zqxt.context_processors.settings',
                'placeholder.context_processor.placeholders',
            ],
        },
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = False
USE_TZ = False

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# upload folder
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


GRAPPELLI_ADMIN_TITLE = u'自强学堂官网'
INTERNAL_IPS = ['127.0.0.1']

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
#COMPRESS_CSS_HASHING_METHOD = 'mtime'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']
COMPRESS_OFFLINE_MANIFEST = "20170519_003049.json"
COMPRESS_ROOT = os.path.join(BASE_DIR, 'static')

# 是否使用CDN库
USE_CDN = True
NOT_USE_CDN = not USE_CDN


########## columns begin ###############
HTML_PAGES = (
    'html', 'js', 'css', 'css3', 'jquery', 'jqueryui',
    'bootstrap', 'jeasyui', 'jquerymobile', 'firebug',
)

WEB_BUILD = (
    'web', 'browsers', 'http', 'hosting', 'tcpip', 'w3c',
    'quality', 'webservices',
)

BROWSER_SCRIPTS = (
    'js', 'jquery', 'jqueryui', 'jquerymobile',
    'jeasyui', 'ajax', 'json', 'googleapi',
)

SERVER_SCRIPTS = (
    'python', 'python3', 'django', 'ruby', 'php',
    'nodejs', 'jsp', 'sql', 'sqlite', 'mysql', 'mongodb',
    'ado', 'asp', 'aspnet',
)

PROG_LANGUAGES = (
    'asp', 'aspnet', 'cprogramming', 'php', 'python',
    'python3', 'java', 'linux', 'ruby', 'vbscript', 'regexp',
)

XML_TUTORIALS = (
    'xml', 'dtd', 'dom', 'xsl', 'xpath', 'xquery', 'xlink',
    'schema', 'soap', 'wsdl', 'rss', 'rdf', 'xslfo', 'svg',
)

########## columns end ###############


# 下面是为了方便在本地调试
if ON_LOCAL_HOST:
    DEBUG = True
    ALLOWED_HOSTS = ['*']

    DEMO_URL = '/demo/'
    DEMO_ROOT = os.path.join(BASE_DIR, 'static/demo')

    STATIC_ROOT = os.path.join(BASE_DIR, 'static2')

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )

    TEMPLATES[0]['OPTIONS']['loaders'] = [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader'
    ]

    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.mysql',
    #         'NAME': 'zqxt',
    #         'USER': 'root',
    #         # 'PASSWORD': '',
    #     }
    # }

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'zqxt.db'
        }
    }

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }
