from django import template
from django.utils.html import mark_safe

from mistune import markdown


register = template.Library()


@register.filter
def render_markdown(markdown_text):
    return mark_safe(markdown(markdown_text, safe_mode="escape"))
