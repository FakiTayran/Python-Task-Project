import uuid
from django.db import models

# Create your models here.
class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,db_index=True)
    plate = models.CharField(max_length=10)
class NavigationRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    datetime1 = models.DateTimeField(db_index=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
