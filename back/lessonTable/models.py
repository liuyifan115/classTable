from django.db import models


# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=100, default=0)
    password = models.CharField(max_length=100, default=0)
    juti = models.CharField(max_length=100, default=0)
    jointeam = models.CharField(max_length=100, default=-1)


class team(models.Model):
    teamname = models.CharField(max_length=100, default=0)
    teamid = models.CharField(max_length=100, default=0)
    member = models.CharField(max_length=100, default='[]')
    table = models.CharField(max_length=100, default='[]')
