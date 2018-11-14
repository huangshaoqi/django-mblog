# -*- coding: utf-8 -*-
"""
@Time    : 2018-11-14-10:45:03
@Author  : hsq10
@File    : urls.py
@Software: PyCharm
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list_page, name='list_page'),
]
