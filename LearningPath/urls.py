from django.conf.urls import patterns, include, url
from django.contrib import admin
from lpath import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^site/', include('lpath.urls')),
)
