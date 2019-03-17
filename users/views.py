from django.views.generic import DetailView

from .models import CustomUser
from blog.models import Tag


class ProfileView(DetailView):
    model = CustomUser
    template_name = "users/author.html"
    context_object_name = "user"
    slug_field = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context
