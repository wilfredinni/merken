from blog.models import Tag
from pages.models import Page
from dashboard.models import SiteConfiguration, HomeMsg


def global_query(request):
    tags = Tag.objects.all()
    pages = Page.objects.all()

    context = {
        "pages": pages,
        "tags": tags,
        "settings": SiteConfiguration.load(),
        # "message": HomeMsg.load(),
    }
    return context
