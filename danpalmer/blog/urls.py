from django.conf.urls import patterns, url

from .feeds import BlogFeed
from .views import Index, View

urlpatterns = patterns(
    '',

    url(r'^blog/?$', Index.as_view(), name='index'),
    url(r'^blog/feed/?$', BlogFeed(), name='feed'),
    url(r'^blog/(?P<slug>[\w-]+)/?$', View.as_view(), name='post'),
)
