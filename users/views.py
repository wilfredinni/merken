from django.views.generic import DetailView

from .models import CustomUser


class ProfileView(DetailView):
    model = CustomUser
    template_name = "merken/users/author.html"
    context_object_name = "user"
    slug_field = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gravatar'] = context['user'].avatar(size=180)
        return context
