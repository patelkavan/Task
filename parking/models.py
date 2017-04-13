from django.db import models

class Spots(models.Model):
	lng = models.DecimalField(blank=False, max_digits=5, decimal_places=2)
	lat = models.DecimalField(blank=False, max_digits=5, decimal_places=2)
	radius = models.CharField(max_length=100)
	occupied = models.BooleanField(default=False)

class Parked(models.Model):
	parking_spot = models.IntegerField(blank=False)
	time_range = models.CharField(max_length=100, blank=True)
