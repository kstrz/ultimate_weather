# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ultimate_weather_site', '0006_auto_20171101_1056'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='temperatures',
            unique_together=set([('service_id', 'date')]),
        ),
    ]