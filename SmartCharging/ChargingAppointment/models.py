from django.db import models
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


