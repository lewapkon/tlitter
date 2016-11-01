# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import RedirectView

from feed.decorators import anonymous_required
from .views import TweetListView, TweetCreateView, TweetDeleteView, RegistrationView

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='index'),
    url(r'^new/$', login_required(TweetCreateView.as_view()), name='new_tweet'),
    url(r'^delete/(?P<pk>\d+)$', login_required(TweetDeleteView.as_view()), name='delete_tweet'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^password-change-done/$', RedirectView.as_view(url=reverse_lazy('index')), name='password_change_done'),
    url(r'^register/$', anonymous_required(RegistrationView.as_view()), name='register'),
]
