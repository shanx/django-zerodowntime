# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_migrations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='safemodel',
            name='field_added',
            field=models.IntegerField(null=True),
        ),
    ]