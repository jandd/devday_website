# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-04 14:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talk', '0011_auto_20170304_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={'ordering': ['title'], 'verbose_name': 'Session', 'verbose_name_plural': 'Sessions'},
        ),
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['name'], 'verbose_name': 'Track', 'verbose_name_plural': 'Tracks'},
        ),
    ]
