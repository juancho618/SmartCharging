from django.db import models

# Create your models here.
class ChargingSpot(models.Model):
    createdDate = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
