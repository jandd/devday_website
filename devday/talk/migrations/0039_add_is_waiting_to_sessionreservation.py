# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-01 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("talk", "0038_auto_20190329_1010")]

    operations = [
        migrations.AddField(
            model_name="sessionreservation",
            name="is_waiting",
            field=models.BooleanField(default=False, verbose_name="On waiting list"),
        )
    ]
