from django.contrib import admin

from .models import SiteConfiguration, HomeMsg


admin.site.register(SiteConfiguration)
admin.site.register(HomeMsg)
