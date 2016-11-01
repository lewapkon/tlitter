# -*- coding: utf-8 -*-
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.models import Person


@python_2_unicode_compatible
class Tweet(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    body = models.CharField(max_length=140)
    timestamp = models.DateTimeField('date published', auto_now=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return '{}: {}'.format(self.author, self.body)
