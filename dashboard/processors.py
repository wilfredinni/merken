from blog.models import Tag
from pages.models import Page


def global_query(request):
    # TODO: site_name must come from the database
    site_name = "Python Cheatsheet"
    tags = Tag.objects.all()
    pages = Page.objects.all()
    context = {
        "site_name": site_name,
        "pages": pages,
        "tags": tags
        }
    return context
