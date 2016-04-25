from django.conf.urls import url, patterns, include
from . import views

urlpatterns = [
    #STORY PROJECT#
    url(r'^story/$', views.story, name='story'),
    url(r'^story_intro/$', views.story_intro, name='story_intro'),
]
