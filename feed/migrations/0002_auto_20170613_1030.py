# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-13 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
    ]
