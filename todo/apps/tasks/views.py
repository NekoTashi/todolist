# -*- coding: utf-8 -*-
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework import permissions

from .serializers import TaskSerializer
from .models import Task


class TaskViewSet(mixins.ListModelMixin,
					mixins.CreateModelMixin,
					mixins.UpdateModelMixin,
					viewsets.GenericViewSet):
	authentication_classes = (authentication.TokenAuthentication, )
	permission_classes = (permissions.IsAuthenticated, )
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

	def get_queryset(self):
		"""
		Get only the user tasks
		"""
		return self.queryset.filter(user=self.request.user)

	def perform_create(self, serializer):
		"""
		Create a task with user pk
		"""
		serializer.save(user=self.request.user)
