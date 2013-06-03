from django.conf.urls import patterns, include, url
from SimplySchedule.views import hello, current, homepage, hours_ahead, http_request_templated_view
from books.views import search_form, search, book_list
from upload.views import upload, upload_thanks, sample_view

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    #  /hello = hello world
    url(r'^hello/$', hello),

    # site root is also hello world for now
    url(r'^$', homepage),

    # Django tutorials
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^time/$', current),
    url(r'^book_list/$', book_list),
    url(r'^httprequest/$', http_request_templated_view), 
    url(r'^search/$', search),
    url(r'^upload/$', upload),
    url(r'^upload/thanks/$', upload_thanks),
    url(r'^sample/$', sample_view),

    # Examples:
    # url(r'^$', 'SimplySchedule.views.home', name='home'),
    # url(r'^SimplySchedule/', include('SimplySchedule.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
