from django.shortcuts import render, get_object_or_404
from .models import Article, Tag


def blog(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "blog.html", context)


def article(request, url):
    article = get_object_or_404(Article, url=url)
    context = {
        "article": article,
    }
    return render(request, "article.html", context)


def article_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, title=tag_name)
    context = {
        "tag": tag,
        }
    return render(request, "tag.html", context)
