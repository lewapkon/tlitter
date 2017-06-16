# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import TweetListView, TweetCreateView, TweetDeleteView, FriendsTweetsView, ToggleLikeView

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='index'),
    url(r'^new/$', login_required(TweetCreateView.as_view()), name='new_tweet'),
    url(r'^delete/(?P<pk>\d+)$', login_required(TweetDeleteView.as_view()), name='delete_tweet'),
    url(r'^friends-tweets/$', login_required(FriendsTweetsView.as_view()), name='friends_tweets'),
    url(r'^toggle_like/(?P<pk>\d+)$', login_required(ToggleLikeView.as_view()), name='toggle_like_tweet'),
]
