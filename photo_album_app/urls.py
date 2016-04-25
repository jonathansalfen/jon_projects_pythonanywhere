from django.conf.urls import url, patterns, include
from . import views
urlpatterns = [
    #OLD WEBSITE#
    url(r'^about/$', views.about, name='about'),
    url(r'^old_index/$', views.old_index, name='old_index'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^contact/$', views.contact, name='contact'),
]

