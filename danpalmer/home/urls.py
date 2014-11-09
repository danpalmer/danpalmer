from django.conf.urls import patterns, url

from .views import Home, CV, CVPDF

urlpatterns = patterns(
    '',

    url(r'^/?$', Home.as_view(), name='view'),
    url(r'^cv(.html)?/?$', CV.as_view(), name='cv'),
    url(r'^cv(.pdf|/pdf)/?$', CVPDF.as_view(), name='cv-pdf'),
)
