# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
import uuid
# Create your models here.
def roomImageFile(instance, filename):
    return '/'.join( ['rooms', str(instance.id), filename] )

class Room(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    members = models.ManyToManyField(User)
    name = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    room_image = models.ImageField(
        upload_to=roomImageFile,
        max_length=254, blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('timestamp',)