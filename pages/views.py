from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404


from .models import Page
from core.models import HomeMsg


class IndexView(ListView):
    model = Page
    template_name = "merken/pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home_page"] = get_object_or_404(Page, slug="index")
        context["message"] = HomeMsg.load()
        return context


class PageView(DetailView):
    model = Page
    template_name = "merken/pages/page.html"
    slug_field = "slug"
