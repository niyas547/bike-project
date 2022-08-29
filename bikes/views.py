from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from bikes.models import bikes

# Create your views here.
class BikeViews(APIView):
    def get(self,request,*args,**kwargs):
        all_bikes=bikes
        if "company" in request.query_params:
            comp=request.query_params.get("company")
            all_bikes=[bike for bike in all_bikes if bike.get("company")==comp]

        if "cubic_capacity" in request.query_params:
            cc=request.query_params.get("cubic_capacity")
            all_bikes=[bike for bike in all_bikes if bike.get("cubic_capacity")==cc]

        if "fuel_capacity" in request.query_params:
            fuel=request.query_params.get("fuel_capacity")
            all_bikes=[bike for bike in all_bikes if bike.get("fuel_capacity")==fuel]

        return Response({"bikes":all_bikes})
    def post(self,request,*args,**kwargs):
        data=request.data
        bikes.append(data)
        return Response({"bikes":"bike added"})


class BikeDetailViews(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        bike=[bike for bike in bikes if bike.get("id")==id].pop()
        return Response({"bike":bike})
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        updated_bike=request.data
        bike=[bike for bike in bikes if bike.get("id")==id].pop()
        bike.update(updated_bike)
        return Response({"bike":"bike updated"})
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        bike=[bike for bike in bikes if bike.get("id")==id].pop()
        bikes.remove(bike)
        return Response({"bike":"bike deleted"})