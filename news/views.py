# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from news.models import Category, Article



# Create your views here.

def index(request):
    nav_display_categories = Category.objects.filter(nav_display=True)
    home_display_categories = Category.objects.filter(home_display=True)
    return render(request, 'index.html', {
        'nav_display_categories': nav_display_categories,
        'home_display_categories': home_display_categories,
    })


def category_detail(request, category_slug):
    # return HttpResponse("Hello, world. You're at the polls index.")
    column = Category.objects.get(slug=category_slug)
    context = {'category', column}
    print context
    return render(request, 'news/category.html', context)


def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)
    if article_slug != article.slug:
        return redirect(article, permanent=True)
    return render(request, 'news/article.html', {'article', article})
