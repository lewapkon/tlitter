# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Person(AbstractUser):
    following = models.ManyToManyField('Person', symmetrical=False)

    class Meta:
        verbose_name_plural = 'people'

    def __str__(self):
        return self.get_full_name()
