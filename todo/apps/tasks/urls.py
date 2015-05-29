# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from rest_framework import routers

from .views import TaskViewSet


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
]
