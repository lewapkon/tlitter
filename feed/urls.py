# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import TweetListView

urlpatterns = [
    url(r'^$', TweetListView.as_view()),
]