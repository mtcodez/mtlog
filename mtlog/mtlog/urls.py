from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mtlog.views.home', name='home'),
    # url(r'^mtlog/', include('mtlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', direct_to_template, {'template': 'log/templates/index.html'}, "home")
    url(r'^$', 'log.views.home_page'),
    url(r'^log_form/', 'log.views.log_form_page'),
    url(r'^about_page/', 'log.views.about_page')
)
