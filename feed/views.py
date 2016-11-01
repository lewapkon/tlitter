# -*- coding: utf-8 -*-

from django.views.generic import ListView

from .models import Tweet


class TweetListView(ListView):
    model = Tweet
    template_name = 'index.html'
    context_object_name = "tweet_list"
    paginate_by = 5
