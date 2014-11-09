import re

from django import template

from danpalmer.blog.models import PostImage

# Match ![]({{ image-slug }})
# Replace ![Image Title](http://image-url)
re_images = re.compile(r'\!\[\]\(\{\{(?P<slug>[ \w-]+)\}\}\)')

register = template.Library()

@register.filter
def render_images(content):
    rendered_content = content

    for match in re_images.finditer(content):
        image = PostImage.objects.get(slug=match.group('slug').strip())

        rendered_content = rendered_content.replace(
            match.group(0),
            '![%s](%s)' % (image.title, image.image.url),
        )

    return rendered_content
