# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
	url(r'^accounts/', include('todo.apps.accounts.urls')),
	url(r'^todo/', include('todo.apps.tasks.urls')),
	url(r'^admin/', include(admin.site.urls)),
]