from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    #NEW WEBSITE#
    url(r'^$', views.index),
    #BLOG PROJECT#
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    #OLD WEBSITE#
    url(r'^about/$', views.about, name='about'),
    url(r'^old_index/$', views.old_index, name='old_index'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^contact/$', views.contact, name='contact'),
    #STORY PROJECT#
    url(r'^story/$', views.story, name='story'),
    url(r'^story_intro/$', views.story_intro, name='story_intro'),
)