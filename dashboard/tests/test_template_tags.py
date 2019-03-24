from django.test import TestCase
from django.template import Template, Context


class MarkdownTag(TestCase):
    TEMPLATE = Template("{% load markdown_tag %} {{ h1|render_markdown}}")

    def test_render_markdown(self):
        context = Context({"h1": "# h1"})
        rendered_template = self.TEMPLATE.render(context)
        self.assertInHTML("<h1>h1</h1>", rendered_template)
