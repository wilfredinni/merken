from apps.blog.models import Tag
from apps.pages.models import Page
from .models import SiteConfiguration


def global_query(request):
    context = {}
    context["settings"] = SiteConfiguration.load()
    context["pages"] = Page.objects.all()
    context["tags"] = Tag.objects.all()
    return context
