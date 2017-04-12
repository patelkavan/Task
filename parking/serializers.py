from rest_framework import serializers
from .models import Spots, Parked

class SpotsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spots
        fields = ('id', 'lng', 'lat', 'occupied')

class ParkedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parked
        fields = ('id', 'parking_spot', 'time_range')