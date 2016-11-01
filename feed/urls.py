# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import url

from .views import TweetListView, TweetCreateView, TweetDeleteView

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='index'),
    url(r'^new/$', TweetCreateView.as_view(), name='new_tweet'),
    url(r'^delete/(?P<pk>\d+)$', TweetDeleteView.as_view(), name='delete_tweet'),
]