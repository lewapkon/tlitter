# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Tweet, Person


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(), label=u'First Name')
    last_name = forms.CharField(widget=forms.TextInput(), label=u'Last Name')

    class Meta:
        model = Person
        fields = ('username', 'first_name', 'last_name')


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['body']
