from django.db import models
import uuid

# Create your models here.

class Operation(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,db_index=True)
    name = models.CharField(max_length=10)

class Bin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    operation = models.ForeignKey(Operation,on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    collection_frequency = models.IntegerField()
    last_collection = models.DateTimeField()
