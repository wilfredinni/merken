from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render


class NeverCacheMixin(object):
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(NeverCacheMixin, self).dispatch(*args, **kwargs)


class DashboardView(NeverCacheMixin, LoginRequiredMixin, TemplateView):
    """Load the VUE app into Django."""
    template_name = "dashboard/dashboard.html"


def handler404(request, exception):
    return render(request, "merken/404.html", status=404)


def handler500(request):
    return render(request, "merken/500.html", status=500)
