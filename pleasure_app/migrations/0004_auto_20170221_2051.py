# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 20:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pleasure_app', '0003_training'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educator',
            name='trained_communication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pleasure_app.Training'),
        ),
    ]
