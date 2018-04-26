# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from backend.permissions import IsOwnerOrReadOnly
from backend.serializers import *


class UserRegisterAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        res = {
            'msg': 'error' # 状态码
            'url': '#'  # 转到链接
        }
        data = request.data
        email = data.get('email')
        password = data.get('password')
        user = User.objects.get(email__exact=email)  # 暂且仅支持email
        if user is not None:
            if user.password == password:
                serializer = UserSerializer(user)
                res['data'] = serializer.data
                res['msg'] = 'welcome'
                res['url'] = '/'
                return Response(res, HTTP_200_OK)
            else:
                res['msg'] = 'password error'
                return Response(res, HTTP_400_BAD_REQUEST)
        else:
            res['msg'] = 'user not exist'
            return Response(res, HTTP_400_BAD_REQUEST)


# class UserLoginAPIView(APIView):
#     """
#     用户登陆API
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (AllowAny, )

#     def post(self, request, format=None):
#         data = request.data
#         username = data.get('name')
#         password = data.get('password')
#         user = User.objects.get(username__exact=username)
#         if user is not None and user.password = password:
#             # success condition
#             serializer = UserSerializer(user)
#             new_data = serializer.data
#             # 记忆已登录用户
#             self.request.session['uid'] = user.id
#             return Response(new_data, status=HTTP_200_OK)
#         else if user is None:
#             # when user not exist
#             return Response('user not exist',HTTP_400_BAD_REQUEST)
#         else if user.password not password:
#             # when password wrong
#             return Response('password error', HTTP_400_BAD_REQUEST)

# class UserRegisterAPIView(APIView):
#     """
#     注册用户
#     """
#     queryset = User.objects.all()
#     serializer_class = UserRegisterSerializer
#     permission_classes = (AllowAny, )

#     def post(self, request, format=None):
#         data = request.data
#         name = data.get('name')
#         if User.objects.filter(name__exact=username):
#             return Response("用户名已存在", HTTP_400_BAD_REQUEST)
#         serializer = UserRegisterSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=HTTP_200_OK)
#         # error condition
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
