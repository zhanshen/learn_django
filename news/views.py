# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from news.models import Category, Article

# Create your views here.

def index(request):
    categorys = Category.objects.all()
    return render(request, 'index.html', {'categorys': categorys})


def category_detail(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    return render(request, 'new/category.html', {'category', category})


def article_detail(request, article_slug):
    article = Article.objects.filter(slug=article_slug)[0]
    return render(request, 'new/article.html', {'article', article})
