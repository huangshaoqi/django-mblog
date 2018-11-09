from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello/([a-z]{2})/$', views.hello, name='hello'),
    url(r'^([0-9]{1})/$', views.number, name='number'),
    url(r'^([a-zA-Z]{1})/$', views.letter, name='letter'),
    url(r'^index/$', views.index, name='index'),
    url(r'^pp/(?P<page>[1-9]+)(?P<p>[a-z]+)/$', views.pp, name='pp'),
    url(r'^form/select/$', views.select, name='select'),
    url(r'^form/add/$', views.add, name='add'),
    url(r'^form/delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^form/modify_1/(?P<id>\d+)$', views.modify_1, name='modify_1'),
    url(r'^form/modify_2/(?P<id>\d+)$', views.modify_2, name='modify_2'),
]
