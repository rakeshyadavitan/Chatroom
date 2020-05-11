# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-07 14:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat_room', '0002_auto_20200506_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='member',
        ),
        migrations.AddField(
            model_name='room',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='room',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='room',
            name='room_image',
            field=models.ImageField(default='rooms_folder/no-img.jpg', upload_to='rooms_folder/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
