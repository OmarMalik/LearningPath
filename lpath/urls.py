from django.conf.urls import patterns, url
from lpath import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        # url(r'^track/(?P<track_name_url>\w+/)$', views.track, name='track'),
        # url(r'^add_track/$', views.add_track, name='add_track'),
)