# -*- coding: utf-8 -*-
from rest_framework import generics
from rest_framework import renderers

from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
	serializer_class = UserSerializer
	renderer_classes = (renderers.JSONRenderer, )
