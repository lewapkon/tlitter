# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout, password_change
from django.urls import reverse_lazy
from django.views.generic import RedirectView

from .forms import MyAuthenticationForm, MyPasswordChangeForm
from .decorators import anonymous_required
from .views import RegistrationView, PersonDetailView, PersonUpdateView, UnfollowView, FollowView

urlpatterns = [
    url(r'^login/$', login, {'authentication_form': MyAuthenticationForm}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^password_change/$', password_change, {'password_change_form': MyPasswordChangeForm}, name='password_change'),
    url(r'^password-change-done/$', RedirectView.as_view(url=reverse_lazy('index')), name='password_change_done'),
    url(r'^register/$', anonymous_required(RegistrationView.as_view()), name='register'),
    url(r'^update-profile/$', login_required(PersonUpdateView.as_view()), name='person_update'),
    url(r'^follow/(?P<pk>\d+)/$', login_required(FollowView.as_view()), name='follow'),
    url(r'^unfollow/(?P<pk>\d+)/$', login_required(UnfollowView.as_view()), name='unfollow'),
    url(r'^(?P<username>[A-Za-z0-9@.+-_]+)/$', PersonDetailView.as_view(), name='person'),
]
