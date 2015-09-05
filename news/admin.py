# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Category, Article

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro', 'nav_display', 'home_display')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'create_time', 'update_time')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
