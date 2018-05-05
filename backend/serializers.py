from rest_framework import serializers
from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = []
        model = Article
        fields = ('pid', 'author', 'title', 'body')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = []
        model = User
        field = ('name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = []
        model = User
        fields = ('name', 'email', 'utype', 'uid')
