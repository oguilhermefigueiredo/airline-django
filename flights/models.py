
from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, blank=True, null=True, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, blank=True, null=True, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: from {self.origin} to {self.destination}."

class Passenger(models.Model):
    f_name = models.CharField(max_length=64)
    l_name = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.f_name.capitalize()} {self.l_name.capitalize()}"
