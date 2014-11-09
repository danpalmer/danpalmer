import datetime

from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=50, unique=True)
    content = models.TextField(default="", blank=True)
    header_image = \
        models.ImageField(null=True, blank=True, upload_to='title_images')
    preview = models.TextField(default="", blank=True)

    published = models.DateTimeField(null=True, blank=True)

    created = models.DateTimeField(
        default=datetime.datetime.utcnow,
        editable=False,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', args=(self.slug,))


class PostImage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='post_images')
    post = models.ForeignKey(Post, related_name='images')

    created = models.DateTimeField(default=datetime.datetime.utcnow)
