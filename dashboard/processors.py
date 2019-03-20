from blog.models import Tag
from pages.models import Page
from dashboard.models import SiteConfiguration


def global_query(request):
    SiteConfiguration.get_solo()

    website = SiteConfiguration.objects.get()
    site_name = website.site_name
    publisher = website.publisher
    canonical_url = website.canonical_url
    site_description = website.site_description
    tags = Tag.objects.all()
    pages = Page.objects.all()

    context = {
        "site_name": site_name,
        "publisher": publisher,
        "canonical_url": canonical_url,
        "site_description": site_description,
        "pages": pages,
        "tags": tags,
    }
    return context
