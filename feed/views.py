# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, FormView

from .forms import TweetForm, RegistrationForm
from .models import Tweet


class RegistrationView(FormView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegistrationView, self).form_valid(form)


class TweetDeleteView(DeleteView):
    model = Tweet

    def get_queryset(self):
        return self.request.user.tweet_set.all()

    def get_object(self, queryset=None):
        tweet = super(TweetDeleteView, self).get_object()
        return tweet

    def get_success_url(self):
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
        context['form'] = TweetForm()
        return context
