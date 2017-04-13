from django.shortcuts import render
from parking.models import Spots, Parked
from parking.serializers import SpotsSerializer, ParkedSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from rest_framework import generics

class SpotList(APIView): #shows all available spots
    def get(self, request, format=None):
        print(request.data)
        spots = Spots.objects.filter(occupied=False)
        serializer = SpotsSerializer(spots, many=True)
        return Response(serializer.data)


class ParkedList(APIView): #lists the parked values
    def get(self, request, format=None):
        parked = Parked.objects.all()
        serializer = ParkedSerializer(parked, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print (request.data["parking_spot"])
        serializer = ParkedSerializer(data=request.data)
        if ReserveIT.get(self, request, pk = request.data["parking_spot"]):
            if serializer.is_valid():
                serializer.save()
                return redirect('/spots/')
        content = {
            'message': "Spot already occupied"
        }
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

class ReserveIT(APIView): #changes the value of the occupied field or pass
    def get(self, request, pk, format=None):
        spots = Spots.objects.get(id=pk)
        print ("serializer['occupied']:",spots.occupied)
        if not spots.occupied:
            spots.occupied = True
            print(spots.occupied)
            spots.save()
            return True
        return False


# http://127.0.0.1:8000/spots/lng=21&lat=19&radius=2
class SpotLngLat(APIView):

    def get(self, request, lng, lat, radius, format=None):
        lng, lat, radius = map(int,[lng, lat, radius])
        print(lat, lng,radius)
        spots = Spots.objects.all()
        serializer = SpotsSerializer(spots, many=True)
        spotlist = []
        for spot in serializer.data:
            spotlng, spotlat = map(float,[spot["lng"],spot["lat"]])
            print(spotlng,spotlat)
            if spotlng in range(lng-radius, lng+radius) and spotlat in range(lat-radius, lat+radius):
                print(spot)
                spotlist.append(spot)
        return Response(spotlist)