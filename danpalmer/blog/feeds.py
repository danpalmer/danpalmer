from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed

from .models import Post


class BlogFeed(Feed):
    title = "Dan Palmer's Blog"
    description = "Software, technology, and anything else I find interesting."
    author_name = "Dan Palmer"
    feed_copyright = settings.COPYRIGHT

    def author_link(self):
        return reverse('home:view')

    def link(self):
        return reverse('blog:index')

    def feed_url(self):
        return reverse('blog:feed')

    def items(self):
        return Post.objects.order_by(
            '-published',
        ).filter(
            published__isnull=False,
        )

    def item_title(self, post):
        return post.title

    def item_description(self, post):
        return post.content
