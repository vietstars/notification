# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-17 13:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20160617_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='friends',
        ),
    ]