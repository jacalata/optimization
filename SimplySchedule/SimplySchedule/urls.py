from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#supposedly only necessary for local development
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView


#pages for simply schedule website
urlpatterns = patterns('upload.views',
    # site root 
    url(r'^$', 'homepage'),
    url(r'^upload/$', 'upload_view'),
    url(r'^sample/$', 'sample_view'),
    url(r'^files/(?P<requested_file>)*', 'file_server_view'),    
    url(r'^home/$', 'homepage'),
    url(r'index.html/$', RedirectView.as_view(url='/home/')),
    url(r'index.php/$', RedirectView.as_view(url='/home/')),
)


# serve static files and show request details while debugging locally
if settings.DEBUG:
    urlpatterns += patterns('SimplySchedule.views',
        url(r'^httprequest/$', 'http_request_templated_view'), 
    )
    urlpatterns += staticfiles_urlpatterns()


# pages from tutorial
urlpatterns += patterns('books.views',
    url(r'^search/$', 'search'),
    url(r'^book_list/$', 'book_list'),
)

#pages from tutorials and practice
urlpatterns += patterns('SimplySchedule.views',
    # Django tutorials
    url(r'^hello/$', 'hello'),
    url(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    url(r'^time/$', 'current'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
