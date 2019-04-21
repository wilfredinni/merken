from blog.models import Tag
from pages.models import Page
from dashboard.models import SiteConfiguration


def global_query(request):
    context = {}
    context["settings"] = SiteConfiguration.load()
    context["pages"] = Page.objects.all()
    context["tags"] = Tag.objects.all()
    return context
