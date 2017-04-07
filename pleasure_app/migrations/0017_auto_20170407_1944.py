# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pleasure_app', '0016_educator_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='educator',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='educator',
            name='living_group',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]