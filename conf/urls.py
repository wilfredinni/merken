from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from apps.blog.sitemaps import ArticleSitemap, BlogSitemap, TagSitemap
from apps.core.views import handler404, handler500
from apps.pages.sitemaps import PagesSitemap
from apps.users.sitemaps import UsersSitemap

sitemaps = {
    "articles": ArticleSitemap,
    "blog": BlogSitemap,
    "page": PagesSitemap,
    "Tags": TagSitemap,
    "users": UsersSitemap,
}

handler404 = handler404
handler500 = handler500

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.core.api.urls")),
    path("accounts/", include("allauth.urls")),
    path("dashboard/", include("apps.core.urls")),
    path("", include("apps.blog.urls")),
    path("", include("apps.users.urls")),
    path("", include("apps.pages.urls")),
    path("robots.txt", include("robots.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
