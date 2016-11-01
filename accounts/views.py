# -*- coding: utf-8 -*-
from __future__ import print_function
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import FormView

from feed.models import Tweet
from .models import Person
from .forms import RegistrationForm


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


class PersonDetailView(DetailView):
    model = Person
    template_name = 'person.html'
    context_object_name = 'person'
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        context['tweets'] = Tweet.objects.filter(author_id=self.get_object().id)
        return context

