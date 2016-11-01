# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import FormView

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
