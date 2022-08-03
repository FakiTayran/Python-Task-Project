from django.shortcuts import render,HttpResponse
from .models import Vehicle,NavigationRecord
from datetime import datetime,timedelta
from django.core.cache import cache

# Create your views here.


now = datetime.now().replace(tzinfo=None)

def home_view(request):
    vehicles =  Vehicle.objects.all()
    vehicles = seedForVehicles(vehicles)

    return render(request,'home.html',{'vehicles':vehicles})

def get_vehicleLocation(request,vehicleid):
    vehiclelocation = NavigationRecord.objects.get(vehicle_id = vehicleid)

    return render(request,'vehiclelocation.html',{'vehiclelocation':vehiclelocation})

def get_vehicleLocations(request):
    last1hourDateTimePK= (now - timedelta(hours=1)).strftime("%Y-%m-%d %H")
    print(last1hourDateTimePK)
    if cache.get(last1hourDateTimePK):
        vehiclelocations = cache.get(last1hourDateTimePK)

    else:
        try:
            lastfortysixhours = now - timedelta(hours=48)

            vehiclelocations = NavigationRecord.objects.filter(datetime1__gte=lastfortysixhours)

            """just for seed database for test"""
            vehiclelocations = seedForVehicleLocations(vehiclelocations)
            """just for seed database for test"""

            cache.set(
                last1hourDateTimePK,
                vehiclelocations
            )
        except:
            return HttpResponse("Something went wrong")


    return render(request,'vehiclelocations.html',{'vehiclelocations':vehiclelocations})


def seedForVehicles(vehicles):

    if len(vehicles) == 0:
        plate = '00 ABC 99'
        Vehicle.objects.create(plate=plate)
        plate = '99 XYZ 000'
        Vehicle.objects.create(plate=plate)

    return vehicles

def seedForVehicleLocations(vehiclelocations):
    if len(vehiclelocations) == 0:
        vehicle = Vehicle.objects.get(plate='00 ABC 99')
        datetime1 = datetime.now().replace(tzinfo=None)
        latitude = 32.32
        longitude = 32.32
        NavigationRecord.objects.create(vehicle=vehicle,datetime1=datetime1,latitude=latitude,longitude=longitude)
        vehicle = Vehicle.objects.get(plate='99 XYZ 000')
        datetime1 = datetime.now().replace(tzinfo=None)
        latitude = 33.33
        longitude = 33.33
        NavigationRecord.objects.create(vehicle=vehicle,datetime1=datetime1,latitude=latitude,longitude=longitude)
        vehicle = Vehicle.objects.get(plate='00 ABC 99')
        datetime1 = datetime.now().replace(tzinfo=None)-timedelta(hours=72)
        latitude = 55.55
        longitude = 55.55
        NavigationRecord.objects.create(vehicle=vehicle, datetime1=datetime1, latitude=latitude, longitude=longitude)
        vehiclelocations = NavigationRecord.objects.filter(datetime1__gte=datetime.now().replace(tzinfo=None)-timedelta(hours=48))

    return vehiclelocations

