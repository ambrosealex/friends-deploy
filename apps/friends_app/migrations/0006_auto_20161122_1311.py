# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 19:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends_app', '0005_auto_20161122_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Friends',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
