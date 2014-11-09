from django.conf.urls import patterns, include, url

from .views import Index

urlpatterns = patterns(
    '',

    url(r'^projects/?$', Index.as_view(), name='index'),

    (r'', include('danpalmer.projects.charts.urls', namespace='charts')),
    (r'', include('danpalmer.projects.complexify.urls', namespace='complexify')),
)
