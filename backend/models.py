# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    """ 用户
    类型：分为管理员、Root管理员、普通用户
    """
    # 用户ID
    # user_id is short by uid
    uid = models.AutoField(primary_key=True)

    # 用户类型
    # 1 普通、2 管理员、3 Root管理
    utype = models.IntegerField(null=False, default=1)

    # 用户名称
    name = models.CharField(max_length=20, null=False)

    # 密码
    password = models.CharField(max_length=20, null=False)


class Article(models.Model):
    """ 文章
    """
    # 文章ID
    pid = models.AutoField(primary_key=True)

    # 作者ID
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题
    title = models.CharField(max_length=250, null=False)

    # 文章内容
    body = models.TextField(null=False)
