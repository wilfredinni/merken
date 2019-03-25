from blog.models import Tag
from pages.models import Page


def global_query(request):
    tags = Tag.objects.all()
    pages = Page.objects.all()

    context = {
        "pages": pages,
        "tags": tags,
    }
    return context
