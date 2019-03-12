from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def blog(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "blog.html", context)


def article(request):
    return HttpResponse("Article page")


def article_by_tag(request):
    return HttpResponse("Articles by tags")
