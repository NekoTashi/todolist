# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('pk', 'name', 'checked', 'created', )
		extra_kwargs = {
			'pk': {'read_only': True},
			'created': {'read_only': True},
		}

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.checked = validated_data.get('checked', instance.checked)
		instance.save()
		return instance
