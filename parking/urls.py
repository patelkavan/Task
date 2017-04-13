from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^spots/$', views.SpotList.as_view(), name='list'),
    url(r'^spots/lng=(?P<lng>[0-9]+)&lat=(?P<lat>[0-9]+)&radius=(?P<radius>[0-9]+)$', views.SpotLngLat.as_view()),
    url(r'^parked/$', views.ParkedList.as_view(), name='parked'),
]
