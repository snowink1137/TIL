from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def index(request):
    return render(request, 'board/index.html')


def greeting(request, name, role):
    if role == 'admin':
        context = {
            'role': 'MASTER USER',
            'name': name,
        }
        return render(request, 'board/greeting.html', context)
    else:
        context = {
            'role': role,
            'name': name,
        }
        return render(request, 'board/greeting.html', context)


# id 불필요
def article_new(request):
    return render(request, 'board/new.html')


def article_create(request):
    article = Article()
    article.title = request.POST.get('input_title')
    article.content = request.POST.get('input_content')
    article.save()
    return render(request, 'board/new.html')


def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'board/list.html', context)


# id 필요
def article_detail(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article
    }

    return render(request, 'board/detail.html', context)


def article_edit(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article,
    }

    return render(request, 'board/edit.html', context)


def article_update(request, id):
    article = Article.objects.get(id=id)
    article.title = request.POST.get('input_title')
    article.content = request.POST.get('input_content')
    article.save()

    return redirect(f'/board_ad/articles/{article.id}')


def article_delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('/board_ad/articles/')
