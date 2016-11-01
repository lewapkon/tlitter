# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import TweetListView, TweetCreateView, TweetDeleteView

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='index'),
    url(r'^new/$', login_required(TweetCreateView.as_view()), name='new_tweet'),
    url(r'^delete/(?P<pk>\d+)$', login_required(TweetDeleteView.as_view()), name='delete_tweet'),
]
