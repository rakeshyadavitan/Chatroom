# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
import uuid
# Create your models here.
class Room(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    members = models.ManyToManyField(User)
    name = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    room_image = models.ImageField(default = 'rooms_folder/no-img.jpg')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('timestamp',)
