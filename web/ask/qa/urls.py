# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question, name='question'),
    url(r'^ask/.*$', views.ask, name='ask'),
    url(r'^popular/.*$', views.popular, name='popular'),
	]