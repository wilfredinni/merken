from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

# from dashboard.views import handler404, handler500

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

# handler404 = handler404
# handler500 = handler500

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

if settings.DEBUG or settings.TESTING_MODE:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
