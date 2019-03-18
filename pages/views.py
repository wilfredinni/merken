from django.views.generic import DetailView


from blog.models import Tag
from .models import Page


def get_all_tags():
    return Tag.objects.all()


class PageView(DetailView):
    model = Page
    template_name = "pages/page.html"
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = get_all_tags()
        return context
