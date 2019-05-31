from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.shortcuts import render


DashboardView = never_cache(TemplateView.as_view(template_name='index.html'))
# class DashboardView(TemplateView):
#     template_name = "index.html"


def handler404(request, exception):
    return render(request, "merken/404.html", status=404)


def handler500(request):
    return render(request, "merken/500.html", status=500)
