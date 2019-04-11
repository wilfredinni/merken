from hashlib import md5
from django import template

register = template.Library()


@register.filter(name='gravatar')
def gravatar(user, size=180):
    digest = md5(user.email.lower().encode("utf-8")).hexdigest()
    return f"https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}"
