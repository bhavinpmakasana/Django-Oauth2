# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 03:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth2', '0027_dailyactivityinformation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DailyActivityInformation',
        ),
    ]
