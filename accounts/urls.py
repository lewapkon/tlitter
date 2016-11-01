# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.urls import reverse_lazy
from django.views.generic import RedirectView

from .views import RegistrationView
from .decorators import anonymous_required

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^password-change-done/$', RedirectView.as_view(url=reverse_lazy('index')), name='password_change_done'),
    url(r'^register/$', anonymous_required(RegistrationView.as_view()), name='register'),
]
