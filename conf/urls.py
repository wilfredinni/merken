from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from apps.core.views import handler404, handler500
from apps.core.sitemaps import (
    ArticleSitemap,
    BlogSitemap,
    TagSitemap,
    PagesSitemap,
    UsersSitemap,
)

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
    path("admin-panel/", admin.site.urls),
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path("api/", include("apps.api.urls")),
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
