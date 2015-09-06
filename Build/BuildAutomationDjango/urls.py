from django.conf.urls import patterns, include, url
from django.contrib import admin
from buildautomation import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BuildAutomationDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^buildautomation/', include('buildautomation.urls')),
    url(r'^$', views.index, name='index'),
)
