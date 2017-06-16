# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import StatisticsView

urlpatterns = [
    url(r'^$', StatisticsView.as_view(), name='statistics'),
]
