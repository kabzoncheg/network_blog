# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogtopic', '0006_auto_20160303_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
