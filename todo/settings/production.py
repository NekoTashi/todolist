# -*- coding: utf-8 -*-
from todo.settings.base import *


DEBUG = False

TEMPLATES[0]['OPTIONS']['loaders'] = [
	('django.template.loaders.cached.Loader', [
		'django.template.loaders.filesystem.Loader',
		'django.template.loaders.app_directories.Loader',
	]),
]
