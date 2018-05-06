# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models


class AdminType(object):
    REGULAR_USER = "Regular User"
    ADMIN = "Admin"
    SUPER_ADMIN = "Super Admin"


class UserSex(object):
    MALE = 'Male'
    FAMALE = 'Famale'


class User(models.Model):
    """用户"""

    # 用户ID
    # user_id is short by uid
    uid = models.AutoField(primary_key=True)

    # 用户类型
    utype = models.TextField(default=AdminType.REGULAR_USER)

    # 性别
    sex = models.TextField(default=UserSex.MALE)

    # 用户名称
    # 不可重复
    username = models.CharField(
        max_length=20, null=False, blank=False, unique=True, db_index=True)

    # 用户昵称
    # 可以重复
    nickname = models.CharField(max_length=20, null=False, blank=False)

    # 用户标签
    nameplate = models.TextField(blank=True)

    # 密码
    # TODO 安全考虑: 此处保存为Hash后的值
    password = models.CharField(max_length=100, blank=False)

    # 邮箱
    # 不可重复
    email = models.EmailField(blank=False, unique=True, db_index=True)

    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True)

    # 最后登陆时间
    last_login_at = models.DateTimeField(auto_now=True)

    # AC数
    ac_num = models.IntegerField(default=0)

    # 提交数
    submit_num = models.IntegerField(default=0)

    def is_admin(self):
        return self.utype == AdminType.ADMIN

    def is_super_admin(self):
        return self.utype == AdminType.SUPER_ADMIN

    def is_admin_role(self):
        return self.utype in [AdminType.ADMIN, AdminType.SUPER_ADMIN]

    def __str__(self):
        return '%ld %s %s' % (self.uid, self.name, self.utype)


class UserProfile(models.Model):

    # OneToOne
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 真名
    realname = models.TextField(null=True)

    # 用户信息
    information = models.TextField(default='这个人什么都没写', null=False, blank=False)

    # Blog链接
    blog = models.URLField()

    # GitHub链接
    github = models.URLField()
