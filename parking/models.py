from django.db import models

class Spots(models.Model):
	lng = models.IntegerField(blank=False, default='')
	lat = models.IntegerField(blank=False, default='')
	radius = models.CharField(max_length=100)
	occupied = models.BooleanField(default=False)

class Parked(models.Model):
	parking_spot = models.IntegerField(blank=False)
	time_range = models.CharField(max_length=100, blank=True)
