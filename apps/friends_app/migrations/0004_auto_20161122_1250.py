# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('friends_app', '0003_auto_20161122_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frined_name', models.CharField(max_length=90)),
                ('friend_alias', models.CharField(max_length=45)),
                ('friend_email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('alias', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=90)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='friends',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friends_app.Users'),
        ),
    ]
