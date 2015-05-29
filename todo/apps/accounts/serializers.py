# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model

from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('pk', 'username', 'email', 'password', )
		extra_kwargs = {
			'password': {'write_only': True },
			'pk': {'read_only': True},
		}

	def create(self, validated_data):
		"""
		Create new user with hashed password
		"""
		user = User.objects.create_user(
			email=validated_data.get('email'),
			username=validated_data.get('username'),
			password=validated_data.get('password')
		)
		return user
