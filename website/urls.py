from django.conf.urls.defaults import patterns, include, url

from website.views import Index
import settings

urlpatterns = patterns(
    '',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', Index.as_view(), name='index'),
    url(r'^detail/(?P<text_id>\w+)/$', 'views.detail'),
    url(r'^upload/$', 'views.upload'),
)

if settings.DEBUG:
    urlpatterns += patterns("",
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,}),
    )
