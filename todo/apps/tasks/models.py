# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User  # TODO: get_model_user()

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Task(models.Model):
	"""
	Represent the user tasks.

	user, name are required. checked is optional.
	"""
	user = models.ForeignKey(User, related_name='tasks')

	name = models.CharField(max_length=128)
	checked = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return 'Task: {0}'.format(self.name.title())
