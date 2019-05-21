from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from blog.sitemaps import ArticleSitemap, BlogSitemap, TagSitemap
from core.views import handler404, handler500
from pages.sitemaps import PagesSitemap
from users.sitemaps import UsersSitemap

sitemaps = {
    "articles": ArticleSitemap,
    "blog": BlogSitemap,
    "page": PagesSitemap,
    "Tags": TagSitemap,
    "users": UsersSitemap
    }

handler404 = handler404
handler500 = handler500

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("", include("users.urls")),
    path("", include("pages.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

if settings.DEBUG or settings.TESTING_MODE:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
