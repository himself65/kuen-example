# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from backend.permission import IsOwnerOrReadOnly
from backend.serializers import *


class ArticleAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    Article APIVie
    """
    queryset = User.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class UserRegisterAPIView(generics.ListCreateAPIView):
    """
    User Register APIView
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class UserAPIView(generics.ListAPIView):
