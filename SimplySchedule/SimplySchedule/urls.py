from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('upload.views',
    url(r'^upload/$', 'upload'),
    url(r'^upload/thanks/$', 'upload_thanks'),
    url(r'^sample/$', 'sample_view'),
)


urlpatterns += patterns('books.views',
    url(r'^search/$', 'search'),
    url(r'^book_list/$', 'book_list'),
)


urlpatterns += patterns('SimplySchedule.views',

    # site root 
    url(r'^$', 'homepage'),

    # Django tutorials
    url(r'^hello/$', 'hello'),
    url(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    url(r'^time/$', 'current'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('SimplySchedule.views',
        url(r'^httprequest/$', 'http_request_templated_view'), 
    )
