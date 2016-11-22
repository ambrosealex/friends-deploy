from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length = 90)
    alias = models.CharField(max_length = 45)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 90)
    birthdate = models.DateField()

class Friends(models.Model):
    user_id = models.ForeignKey(Users)
    friend_id = models.ForeignKey(Users, related_name = 'friend')
