from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

# from django_google_maps import fields as map_fields

class Pin(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 200)
    lat = models.FloatField(default = 0)
    long = models.FloatField(default = 0)
    date = models.DateField(default = datetime.date.today)
    purpose = models.CharField(max_length = 200, default='')
    rating = models.IntegerField(default=5)
    note = models.CharField(max_length = 500, default='')
    user = models.ManyToManyField(User)
    # this is for django_google_maps
    # gmap_address = map_fields.AddressField(max_length=200)
    # gmap_geolocation = map_fields.GeoLocationField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('show', kwargs={'pin_id': self.id})