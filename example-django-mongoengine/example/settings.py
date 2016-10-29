"""
Django settings for example project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

import mongoengine

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v*kswpdyi3+*-=q4a)7&_!xwb%@udm1vi56r690!!j6e*p3^mn'

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
    'django_jinja',
    'django_mongoengine.mongo_auth',
    'social_django',
    'app'
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

ROOT_URLCONF = 'example.urls'

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(BASE_DIR, 'common', 'templates')
        ],
        'OPTIONS': {
            'match_extension': '.html',
            'match_regex': r'^(?!admin/).*',
            'filters': {
                'backend_name': 'common.filters.backend_name',
                'backend_class': 'common.filters.backend_class',
                'icon_name': 'common.filters.icon_name',
                'social_backends': 'common.filters.social_backends',
                'legacy_backends': 'common.filters.legacy_backends',
                'oauth_backends': 'common.filters.oauth_backends',
                'filter_backends': 'common.filters.filter_backends',
                'slice_by': 'common.filters.slice_by'
            },
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
            ],
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = 'example.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.amazon.AmazonOAuth2',
    'social_core.backends.angel.AngelOAuth2',
    'social_core.backends.aol.AOLOpenId',
    'social_core.backends.appsfuel.AppsfuelOAuth2',
    'social_core.backends.beats.BeatsOAuth2',
    'social_core.backends.behance.BehanceOAuth2',
    'social_core.backends.belgiumeid.BelgiumEIDOpenId',
    'social_core.backends.bitbucket.BitbucketOAuth',
    'social_core.backends.box.BoxOAuth2',
    'social_core.backends.clef.ClefOAuth2',
    'social_core.backends.coinbase.CoinbaseOAuth2',
    'social_core.backends.coursera.CourseraOAuth2',
    'social_core.backends.dailymotion.DailymotionOAuth2',
    'social_core.backends.deezer.DeezerOAuth2',
    'social_core.backends.disqus.DisqusOAuth2',
    'social_core.backends.douban.DoubanOAuth2',
    'social_core.backends.dropbox.DropboxOAuth',
    'social_core.backends.dropbox.DropboxOAuth2',
    'social_core.backends.eveonline.EVEOnlineOAuth2',
    'social_core.backends.evernote.EvernoteSandboxOAuth',
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.fedora.FedoraOpenId',
    'social_core.backends.fitbit.FitbitOAuth2',
    'social_core.backends.flickr.FlickrOAuth',
    'social_core.backends.foursquare.FoursquareOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GooglePlusAuth',
    'social_core.backends.google.GoogleOpenIdConnect',
    'social_core.backends.instagram.InstagramOAuth2',
    'social_core.backends.jawbone.JawboneOAuth2',
    'social_core.backends.kakao.KakaoOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth',
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.live.LiveOAuth2',
    'social_core.backends.livejournal.LiveJournalOpenId',
    'social_core.backends.mailru.MailruOAuth2',
    'social_core.backends.mendeley.MendeleyOAuth',
    'social_core.backends.mendeley.MendeleyOAuth2',
    'social_core.backends.mineid.MineIDOAuth2',
    'social_core.backends.mixcloud.MixcloudOAuth2',
    'social_core.backends.nationbuilder.NationBuilderOAuth2',
    'social_core.backends.odnoklassniki.OdnoklassnikiOAuth2',
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.openstreetmap.OpenStreetMapOAuth',
    'social_core.backends.persona.PersonaAuth',
    'social_core.backends.podio.PodioOAuth2',
    'social_core.backends.rdio.RdioOAuth1',
    'social_core.backends.rdio.RdioOAuth2',
    'social_core.backends.readability.ReadabilityOAuth',
    'social_core.backends.reddit.RedditOAuth2',
    'social_core.backends.runkeeper.RunKeeperOAuth2',
    'social_core.backends.sketchfab.SketchfabOAuth2',
    'social_core.backends.skyrock.SkyrockOAuth',
    'social_core.backends.soundcloud.SoundcloudOAuth2',
    'social_core.backends.spotify.SpotifyOAuth2',
    'social_core.backends.stackoverflow.StackoverflowOAuth2',
    'social_core.backends.steam.SteamOpenId',
    'social_core.backends.stocktwits.StocktwitsOAuth2',
    'social_core.backends.stripe.StripeOAuth2',
    'social_core.backends.suse.OpenSUSEOpenId',
    'social_core.backends.thisismyjam.ThisIsMyJamOAuth1',
    'social_core.backends.trello.TrelloOAuth',
    'social_core.backends.tripit.TripItOAuth',
    'social_core.backends.tumblr.TumblrOAuth',
    'social_core.backends.twilio.TwilioAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.vk.VKOAuth2',
    'social_core.backends.weibo.WeiboOAuth2',
    'social_core.backends.wunderlist.WunderlistOAuth2',
    'social_core.backends.xing.XingOAuth',
    'social_core.backends.yahoo.YahooOAuth',
    'social_core.backends.yahoo.YahooOpenId',
    'social_core.backends.yammer.YammerOAuth2',
    'social_core.backends.yandex.YandexOAuth2',
    'social_core.backends.vimeo.VimeoOAuth1',
    'social_core.backends.lastfm.LastFmAuth',
    'social_core.backends.moves.MovesOAuth2',
    'social_core.backends.vend.VendOAuth2',
    'social_core.backends.email.EmailAuth',
    'social_core.backends.username.UsernameAuth',
    'social_core.backends.upwork.UpworkOAuth',
    'django_mongoengine.auth.MongoEngineBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/done/'
SOCIAL_AUTH_STRATEGY = 'social_django.strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social_django_mongoengine.models.DjangoStorage'
SOCIAL_AUTH_GOOGLE_OAUTH_SCOPE = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/userinfo.profile'
]
SOCIAL_AUTH_EMAIL_FORM_HTML = 'email_signup.html'
SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION = 'app.mail.send_validation'
SOCIAL_AUTH_EMAIL_VALIDATION_URL = '/email-sent/'
SOCIAL_AUTH_USERNAME_FORM_HTML = 'username_signup.html'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'app.pipeline.require_email',
    'social_core.pipeline.mail.mail_validation',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.debug.debug',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.debug.debug'
)

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy'
    }
}

AUTH_USER_MODEL = 'mongo_auth.MongoUser'
MONGOENGINE_USER_DOCUMENT = 'django_mongoengine.auth.User'
SESSION_ENGINE = 'django_mongoengine.sessions'
SESSION_SERIALIZER = 'django_mongoengine.sessions.BSONSerializer'

mongoengine.connect('psa', host='mongodb://localhost/psa-django-me')

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

try:
    from example.local_settings import *
except ImportError:
    pass