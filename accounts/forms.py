# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm

from .models import Person


class RegistrationForm(UserCreationForm):
    username = UsernameField(
        max_length=150,
        label='',
        widget=forms.TextInput(attrs={'autofocus': '',
                                      'placeholder': 'Username',
                                      'class': 'form-control'}),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First name',
                                      'class': 'form-control'}),
        label=''
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Last name',
                                      'class': 'form-control'}),
        label=''
    )
    password1 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                          'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation',
                                          'class': 'form-control'}),
        strip=False,
    )

    class Meta:
        model = Person
        fields = ('username', 'first_name', 'last_name')


class MyAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        max_length=254,
        label='',
        widget=forms.TextInput(attrs={'autofocus': '',
                                      'placeholder': 'Username',
                                      'class': 'form-control'}),
    )
    password = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                          'class': 'form-control'}),
    )


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': '',
                                          'placeholder': 'Old password',
                                          'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'New password',
                                          'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'New password confirmation',
                                          'class': 'form-control'}),
    )


class PersonUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First name',
                                      'class': 'form-control'}),
        label=''
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Last name',
                                      'class': 'form-control'}),
        label=''
    )

    class Meta:
        model = Person
        fields = ['first_name', 'last_name']
