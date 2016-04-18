# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 11:31
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Текст')),
            ],
        ),
    ]