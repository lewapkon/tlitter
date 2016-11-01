# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.forms import ModelForm

from .models import Tweet


class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['body']