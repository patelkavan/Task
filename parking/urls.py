from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^spots/$', views.SpotList.as_view(), name='list'),
    url(r'^parked/$', views.ParkedList.as_view(), name='parked'),
]
