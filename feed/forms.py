# -*- coding: utf-8 -*-
from django import forms

from .models import Tweet


class TweetForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "What's happening?", 'class': 'form-control'}))

    class Meta:
        model = Tweet
        fields = ['body']
