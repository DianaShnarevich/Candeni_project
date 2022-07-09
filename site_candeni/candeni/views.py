from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import *

menu = [{'title': 'О НАС', 'url_name': 'about'},
        {'title': 'СТАТЬИ', 'url_name': 'content'},
        # {'title': 'НАШИ ПРОЕКТЫ', 'url_name': 'add_page'},
        {'title': 'ОТЗЫВЫ', 'url_name': 'comment'},
        {'title': 'КОНТАКТЫ', 'url_name': 'contact'},
        ]


def index(request):
    posts = Furniture.objects.all()
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0
    }
    return render(request, "candeni/index.html", context=context)


def about(request):
    return render(request, "candeni/about.html", {'menu': menu, 'title': 'О НАС'})

#
# def addpage(request):
#     return HttpResponse("наши проекты")


def content(request):
    content = Content.objects.all()
    context = {
        'content': content,
        'menu': menu,
        'title': 'Главная страница'
        # 'cat_selected': 0
    }
    return render(request, "candeni/postscandeni.html", context=context)


def comment(request):
    comment = Comment.objects.all()
    context = {
        'comment': comment,
        'menu': menu,
        'title': 'Главная страница'
        # 'cat_selected': 0
    }
    return render(request, "candeni/comment.html", context=context)


def contact(request):
    return HttpResponse("Обратная связь")


def show_post(request, post_slug):
    post = get_object_or_404(Furniture, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'name': post.name,
        'cat_selected': 1,
    }
    return render(request, 'candeni/post.html', context=context)


def show_category(request, cat_id):
    posts = Furniture.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id
    }
    return render(request, "candeni/index.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена<h1>")

