# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

USER_TYPE = (
    ('1', '普通用户'),
    ('2', '管理员'),
    ('3', 'Root管理员'),
)


class User(models.Model):
    """ 用户
    类型：分为管理员、Root管理员、普通用户
    """
    # 用户ID
    # user_id is short by uid
    uid = models.AutoField(primary_key=True)

    # 用户类型
    # 1 普通、2 管理员、3 Root管理
    utype = models.CharField(max_length=1, choices=USER_TYPE, blank=False)

    # 用户名称
    name = models.CharField(max_length=20, null=False, blank=False)

    # 密码
    # TODO 安全考虑: 此处保存为Hash后的值
    password = models.CharField(max_length=100, blank=False)

    # 邮箱
    email = models.EmailField(unique=True, blank=False)

    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%ld %s %s' % (self.uid, self.name, self.utype)


class Article(models.Model):
    """ 文章
    """
    # 文章ID
    pid = models.AutoField(primary_key=True)

    # 作者ID
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    # 文章标题
    title = models.CharField(max_length=250, null=False, blank=False)

    # 文章内容
    body = models.TextField(null=False, blank=False)

    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%ld %s %s' % (self.pid, self.title, self.author)
