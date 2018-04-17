# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    # 文章ID
    pid = models.AutoField(primary_key=True)

    # 作者ID
    authorID = models.IntegerField()

    # 文章标题
    title = models.CharField(max_length=250)

    # 文章内容
    body = models.TextField()
