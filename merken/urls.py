from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

from dashboard.sitemaps import (
    StaticViewSitemap,
    # ArticleSitemap,
    # PageSitemap,
    # TagSitemap,
)

sitemaps = {
    "static": StaticViewSitemap,
    # "article": ArticleSitemap,
    # "tag": TagSitemap,
    # "page": PageSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("", include("users.urls")),
    path("", include("pages.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps}
    ),
]
