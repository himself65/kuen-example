from rest_framework import serializers
from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = []
        model = Article
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = []
        model = User
        field = ('name', 'email')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = []
        model = User
        fields = ('name', 'email', 'utype', 'uid')
