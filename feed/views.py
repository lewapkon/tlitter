# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView

from .models import Tweet, Person
from .forms import TweetForm


class TweetDeleteView(DeleteView):
    model = Tweet

    def get_queryset(self):
        return self.request.user.tweet_set.all()

    def get_object(self, queryset=None):
        tweet = super(TweetDeleteView, self).get_object()
        return tweet

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse('index')


class TweetCreateView(CreateView):
    model = Tweet
    form_class = TweetForm

    def form_valid(self, form):
        if not self.request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        candidate = form.save(commit=False)
        candidate.author = self.request.user
        candidate.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('index')


class TweetListView(ListView):
    model = Tweet
    template_name = 'index.html'
    context_object_name = "tweet_list"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(TweetListView, self).get_context_data(**kwargs)
        context['new_tweet_form'] = TweetForm()
        return context


class FriendsTweetsView(ListView):
    model = Tweet
    template_name = 'friends-tweets.html'
    context_object_name = "tweet_list"
    paginate_by = 5

    def get_queryset(self):
        return Tweet.objects.filter(author__in=Person.objects.get(pk=self.request.user.pk).following.all())
