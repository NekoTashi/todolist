# -*- coding: utf-8 -*-
from todo.settings.base import *


INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

INTERNAL_IPS = (
	'127.0.0.1',
)

DEBUG_TOOLBAR_CONFIG = {
	'INTERCEPT_REDIRECTS': False,
	'SHOW_TEMPLATE_CONTEXT': True,
	'HIDE_DJANGO_SQL': False,
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
