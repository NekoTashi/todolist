# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework import test
from rest_framework.authtoken.models import Token


User = get_user_model()


class UserRegisterViewTestCase(test.APITestCase):
	def setUp(self):
		self.client = test.APIClient()

	def test_create_user(self):
		"""
		Test the user creation.
		"""
		url = reverse('user-register')
		data = {
			'username': 'testuser',
			'password': 'testpass',
			'email': 'test@test.com'
		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ObtainAuthTokenViewTestCase(test.APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			username='testuser',
			password='testpass',
			email='test@test.com'
		)
		self.token = Token.objects.get(user=self.user)
		self.client = test.APIClient()

	def test_obtain_auth_token(self):
		"""
		Test get auth token.
		"""
		url = reverse('api-token-auth')
		data = {
			'username': self.user.username,
			'password': 'testpass',
		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.data['token'], self.token.key)
