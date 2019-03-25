from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import SiteConfiguration, HomeMsg


admin.site.register(SiteConfiguration, SingletonModelAdmin)
admin.site.register(HomeMsg, SingletonModelAdmin)
