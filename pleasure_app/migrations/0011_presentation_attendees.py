# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pleasure_app', '0010_auto_20170223_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='attendees',
            field=models.IntegerField(default=0),
        ),
    ]
