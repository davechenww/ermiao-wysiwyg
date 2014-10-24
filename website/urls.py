from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from website.views import Index, Create, Detail, Upload

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', Index.as_view(), name='index'),
    url(r'^create/$', Create.as_view(), name='create'),
    url(r'^detail/(?P<_id>\w+)/$', Detail.as_view(), name='detail'),
    url(r'^upload/$', Upload.as_view(), name='upload'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
