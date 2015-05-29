# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework import test
from rest_framework.authtoken.models import Token
from .models import Task


User = get_user_model()


class TaskViewSetTestCase(test.APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			username='testuser',
			password='testpass',
			email='test@test.com'
		)
		self.token = Token.objects.get(user=self.user)

		self.client = test.APIClient()
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

	def test_list_task_viewset(self):
		"""
		Test list the user tasks.
		"""
		url = reverse('task-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_create_task_viewset(self):
		"""
		Test create a user task.
		"""
		url = reverse('task-list')
		data = {'name': 'test task create name'}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_update_task_viewset(self):
		"""
		Test update a user task.
		"""
		test_task = Task.objects.create(user=self.user,
										name='test task update name')
		
		detail_url = reverse('task-detail', kwargs={'pk': test_task.pk})
		data_to_update = {'checked': True}
		response = self.client.patch(detail_url,
										data_to_update,
										format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
