# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import RedirectView

from .views import RegistrationView, PersonDetailView, PersonEditView, UnfollowView, FollowView
from .decorators import anonymous_required

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^password-change-done/$', RedirectView.as_view(url=reverse_lazy('index')), name='password_change_done'),
    url(r'^register/$', anonymous_required(RegistrationView.as_view()), name='register'),
    url(r'^update-profile/$', login_required(PersonEditView.as_view()), name='person_update'),
    url(r'^follow/(?P<pk>\d+)/$', login_required(FollowView.as_view()), name='follow'),
    url(r'^unfollow/(?P<pk>\d+)/$', login_required(UnfollowView.as_view()), name='unfollow'),
    url(r'^(?P<slug>[A-Za-z0-9@.+-_]+)/$', PersonDetailView.as_view(), name='person'),
]
