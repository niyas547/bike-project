from django.db import models

# Create your models here.
class Bikes(models.Model):
    name=models.CharField(max_length=120)
    company=models.CharField(max_length=120)
    cubic_capacity=models.CharField(max_length=120)
    price=models.PositiveIntegerField()
    fuel_capacity=models.CharField(max_length=120)
    mileage=models.CharField(max_length=120)
    rating=models.FloatField(null=True,default=4.5)

