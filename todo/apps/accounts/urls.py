# -*- coding: utf-8 -*-
from django.conf.urls import url

from rest_framework.authtoken import views

from .views import RegisterView


urlpatterns = [
	url(r'^api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
	url(r'^', RegisterView.as_view(), name='user-register'),
]
