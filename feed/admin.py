# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Tweet, Person

admin.site.register(Tweet)
admin.site.register(Person, UserAdmin)
