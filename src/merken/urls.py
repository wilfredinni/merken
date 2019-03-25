from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
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

if settings.DEBUG or settings.TESTING_MODE:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    print(settings.STATIC_URL)
    print(settings.STATIC_ROOT)
