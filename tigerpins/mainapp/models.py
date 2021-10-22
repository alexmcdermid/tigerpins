from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django_google_maps import fields as map_fields



class Locations(models.Model):
    locationName = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()
    #this is for django_google_maps
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)


    user = models.ManyToManyField(User)


