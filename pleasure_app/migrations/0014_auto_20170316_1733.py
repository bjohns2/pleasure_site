# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pleasure_app', '0013_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(null=True, to='pleasure_app.Educator'),
        ),
    ]