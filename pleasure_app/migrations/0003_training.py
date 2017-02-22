# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pleasure_app', '0002_auto_20170221_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(choices=[('COM', 'Communication'), ('VAL', 'Values'), ('ID', 'Identity'), ('LOV', 'Love'), ('CUL', 'Culture')], max_length=3)),
                ('date', models.DateField()),
                ('notes', models.TextField()),
            ],
        ),
    ]
