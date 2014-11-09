from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

urlpatterns = patterns(
    '',

    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    (r'', include('danpalmer.home.urls', namespace='home')),
    (r'', include('danpalmer.blog.urls', namespace='blog')),
    (r'', include('danpalmer.projects.urls', namespace='projects')),
)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
