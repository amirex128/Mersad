from django.db import models


# Create your models here.
class Patrol(models.Model):
    team_realm = models.CharField(max_length=500)
    team_base = models.CharField(max_length=500)
    charges = models.CharField(max_length=500)
    leader = models.CharField(max_length=500)
    responsibility_leader = models.CharField(max_length=500)
    patrol_started_at = models.CharField(max_length=500)
    serial_ruling = models.CharField(max_length=500)
    ruling_started_at = models.CharField(max_length=500)
    area = models.CharField(max_length=500)
    realm = models.CharField(max_length=500)
    teams = models.CharField(max_length=500)
    time_started_at = models.CharField(max_length=500)
    time_ended_at = models.CharField(max_length=500)
    places = models.CharField(max_length=500)
