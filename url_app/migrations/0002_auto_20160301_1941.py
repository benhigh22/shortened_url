# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-01 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='shortened_url',
            field=models.CharField(max_length=100),
        ),
    ]
