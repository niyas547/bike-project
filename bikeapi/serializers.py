from rest_framework import serializers
from bikeapi.models import Bikes
class BikesSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    company=serializers.CharField()
    cubic_capacity=serializers.CharField()
    price=serializers.IntegerField()
    fuel_capacity=serializers.CharField()
    mileage=serializers.CharField()
    rating=serializers.FloatField()

class BikeModelSerializer(serializers.ModelSerializer):
    class Meta:
        id=serializers.CharField(read_only=True)
        model=Bikes
        fields="__all__"
