# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import AbstractUser


@python_2_unicode_compatible
class Person(AbstractUser):
    class Meta:
        verbose_name_plural = 'people'

    def __str__(self):
        return self.get_full_name()


@python_2_unicode_compatible
class Tweet(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    body = models.CharField(max_length=140)
    timestamp = models.DateTimeField('date published')

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return '{}: {}'.format(self.author, self.body)
