from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Locations(models.Model):
    locationName = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()

    user = models.ManyToManyField(User)


print("THIS IS THE CHANGE I AM MAKING")