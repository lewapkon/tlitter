# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):
    pass


class Tweet(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    body = models.CharField(max_length=140)
    timestamp = models.DateTimeField('date published')
