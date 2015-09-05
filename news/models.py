# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse
# Create your models here.

# 栏目
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField('栏目名称', max_length=256)
    slug = models.CharField('栏目网址', max_length=256, unique=True)
    intro = models.TextField('栏目简介', default='')

    nav_display = models.BooleanField('导航显示', default=False)
    home_display = models.BooleanField('首页显示', default=False)

    def get_absolute_url(self):
        return reverse('category', args=(self.slug,))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']  # 按照哪个栏目排序


# 文章
@python_2_unicode_compatible
class Article(models.Model):
    # 文章和栏目是多对多映射
    column = models.ManyToManyField(Category, verbose_name='归属栏目')

    # id 这个是默认有的，也可以自己定义一个其它的主键来覆盖它
    id = models.AutoField(primary_key=True)

    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256, unique=True)

    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')
    content = UEditorField('内容', height=300, width=1000, default=u'', blank=True,
                           imagePath="uploads/images/", toolbars='besttome',
                           filePath='uploads/files/')

    published = models.BooleanField('正式发布', default=True)
    create_time = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def get_absolute_url(self):
        return reverse('article', args=(self.pk, self.slug,))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'
