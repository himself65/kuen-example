# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models


class Article(models.Model):
    """文章"""

    # 文章ID
    aid = models.AutoField(primary_key=True)

    # 作者ID
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    # 文章标题
    title = models.CharField(max_length=80, default='')

    # 文章内容
    content = models.TextField(default='')

    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True)

    # 最后修改时间
    update_at = models.DateTimeField(auto_now=True)

    # 允许评论
    allow_comment = models.BooleanField(default=True)

    # 评论数量
    comments_num = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-update-at']
