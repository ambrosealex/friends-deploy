# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 19:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends_app', '0004_auto_20161122_1250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friends',
            old_name='frined_name',
            new_name='friend_name',
        ),
    ]