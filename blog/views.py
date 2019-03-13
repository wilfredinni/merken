from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Article, Tag


class BlogView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog.html"


class ArticleView(DetailView):
    model = Article
    template_name = "article.html"
    slug_field = "url"


# def article(request, url):
#     article = get_object_or_404(Article, url=url)
#     context = {"article": article}
#     return render(request, "article.html", context)


def article_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, title=tag_name)
    articles = tag.article_set.all()
    context = {"articles": articles}
    return render(request, "tag.html", context)
