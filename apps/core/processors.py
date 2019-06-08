from apps.blog.models import Tag, Article
from apps.pages.models import Page
from .models import SiteConfiguration


def global_query(request):
    context = {}
    context["settings"] = SiteConfiguration.load()
    context["pages"] = Page.objects.all()
    context["tags"] = Tag.objects.all()
    context["featured"] = Article.objects.featured()
    return context
