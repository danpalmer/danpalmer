from django.conf.urls import patterns, url

from .views import Index

urlpatterns = patterns(
    '',

    url(r'^projects/jquery-complexify/?$', Index.as_view(), name='view'),

    # Legacy
    url(r'^jquery-complexify(/(index.html)?)?$', Index.as_view()),
)
