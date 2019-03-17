from django.views.generic import DetailView

from .models import CustomUser


class ProfileView(DetailView):
    model = CustomUser
    template_name = "users/profile.html"
    context_object_name = "user"
    slug_field = "username"
