# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-06 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_room', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='id',
        ),
        migrations.AlterField(
            model_name='room',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False),
        ),
    ]