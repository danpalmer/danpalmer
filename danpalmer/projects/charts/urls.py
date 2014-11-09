from django.conf.urls import patterns, url

from .views import Index

urlpatterns = patterns(
    '',

    url(r'^projects/django-google-charts/?$', Index.as_view(), name='view'),
)
