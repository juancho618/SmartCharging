from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from  django.core.urlresolvers import reverse


class PlugType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):             #Return after the save or edit action!
        return  reverse("listPlugType")


# Create your models here.
class ChargingSpot(models.Model):
    createdDate = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    isFast = models.BooleanField(default=False)
    defect = models.BooleanField(default=False)
    hasOwner = models.BooleanField(default=False)
    price = models.FloatField(default=0)
    plugType = models.ForeignKey(PlugType)
    latitude = models.CharField(max_length=255, default=0)
    longitude = models.CharField(max_length=255, default=0)
    country = models.CharField(max_length=255, default=0)
    city = models.CharField(max_length=255, default=0)
    area = models.CharField(max_length=255, default=0)
    neighborhood = models.CharField(max_length=255, default=0)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):             #Return after the save or edit action!
        return reverse("chargingSpotsList")

class Appointment (models.Model):
    creationDate = models.DateTimeField(auto_now_add=True)
    chargingStation = models.ForeignKey(ChargingSpot)
    reservationDate = models.DateTimeField(null=False)
    userReservation = models.ForeignKey(settings.AUTH_USER_MODEL)

    def get_absolute_url(self):
        return reverse('listPlugType')

class ChargingStationRate(models.Model):
    chargingStation = models.ForeignKey(ChargingSpot)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    rate = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    comment = models.CharField(max_length=255)
    creationDate = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):  # Return after the save or edit action!
        return reverse("detailsChargingStation", kwargs={'pk':self.chargingStation.pk})

