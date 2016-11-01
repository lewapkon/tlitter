# -*- coding: utf-8 -*-
from __future__ import print_function

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, FormView, UpdateView

from feed.models import Tweet
from .forms import RegistrationForm
from .models import Person


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


class PersonEditView(UpdateView):
    template_name = 'registration/person_update.html'
    fields = ['first_name', 'last_name']

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('person', kwargs={'slug': self.get_object().username})


class PersonDetailView(DetailView):
    model = Person
    template_name = 'person.html'
    context_object_name = 'person'
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        person = self.get_object()
        context['tweets'] = Tweet.objects.filter(author_id=person.id)
        context['person_name'] = person.get_username() + "'s"
        context['follows'] = self.request.user.following.filter(pk=person.pk).exists()
        return context


class FollowView(View):
    def post(self, request, *args, **kwargs):
        other_person = Person.objects.get(pk=kwargs['pk'])
        if not request.user.following.filter(pk=kwargs['pk']).exists():
            Person.objects.get(pk=request.user.pk).following.add(other_person)
        return HttpResponseRedirect(reverse_lazy('person', kwargs={'slug': other_person.username}))


class UnfollowView(View):
    def post(self, request, *args, **kwargs):
        other_person = Person.objects.get(pk=kwargs['pk'])
        if request.user.following.filter(pk=kwargs['pk']).exists():
            Person.objects.get(pk=request.user.pk).following.remove(other_person)
        return HttpResponseRedirect(reverse_lazy('person', kwargs={'slug': other_person.username}))
