from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from bikeapi.serializers import BikesSerializer
from bikeapi.models import Bikes
from bikeapi.serializers import BikeModelSerializer

# Create your views here.

class BikeView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Bikes.objects.all()
        if "company" in request.query_params:
            qs=qs.filter(company=request.query_params.get("company"))
        if "cubic_capacity" in request.query_params:
            qs=qs.filter(cubic_capacity=request.query_params.get("cubic_capacity"))
        if "fuel_capacity" in request.query_params:
            qs=qs.filter(fuel_capacity=request.query_params.get("fuel_capacity"))

        serializer=BikesSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=BikesSerializer(data=request.data)
        if serializer.is_valid():
            Bikes.objects.create(**serializer.validated_data)
            return Response(data=serializer.validated_data)
        else:
            return Response(data=serializer.errors)


class BikeDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Bikes.objects.get(id=id)
        serializer=BikesSerializer(qs)
        return Response(data=serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Bikes.objects.filter(id=id)
        serializer=BikesSerializer(data=request.data)
        if serializer.is_valid():
            qs.update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Bikes.objects.get(id=id)
        qs.delete()
        return Response({"message":"bike deleted"})


class BikeModelView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Bikes.objects.all()
        serializer=BikeModelSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=BikeModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class BikeModelDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Bikes.objects.get(id=id)
        serializer=BikeModelSerializer(qs)
        return Response(data=serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Bikes.objects.get(id=id)
        serializer=BikeModelSerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)




