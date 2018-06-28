from .base import *

ALLOWED_HOSTS = ['*', ]

DEBUG = True
INTERNAL_IPS = ('127.0.0.1', 'localhost',)
# MIDDLEWARE_CLASSES += (
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# )

# INSTALLED_APPS += (
#     'debug_toolbar',
# )

# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
# ]

# DEBUG_TOOLBAR_CONFIG = {
#     'INTERCEPT_REDIRECTS': False,
# }

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',     # config('DB_PASSWORD'),
        'PORT': '',
        'USER': ''          # config('DB_USER')
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_USE_TLS = True

# EMAIL_PORT = 587
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'dmw.contacts@gmail.com'
# EMAIL_HOST_PASSWORD = 'd_m_w_tr@ve1'
# EMAIL_USE_TLS = True

# DEBUG_TOOLBAR_CONFIG = {
#     'JQUERY_URL': '',
# }
