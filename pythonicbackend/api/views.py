from .models import Driver, ScheduledDate, DriverManager, ScheduledDatesManager, Images, Vehicles, Invoice, managers, VehicleDamages, SupportType, DeductionType, VehicleScheduledDate
from rest_framework.response import Response
from rest_framework.views import APIView, View
from rest_framework import viewsets
import json
import base64
from rest_framework.permissions import IsAuthenticated
from .serializers import managersSerializer, DriverSerializer, ScheduledDatesSerializer, ImagesSerializer, VehiclesSerializer, InvoiceSerializer, VehicleDamagesSerializer, SupportTypeSerializer, DeductionTypeSerializer, VehicleScheduledDateSerializer
from .functions import timeDifference, returnOrderdData, statistics, invoice, returnVanOrderedData, tokenizer, complianceCheck, addDatedDriver, documentsDriversOnly, dailyService
from .test_data import importData
import csv, io 
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class managersViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)

    # Users
    queryset = managers.objects.all()
    serializer_class = managersSerializer

class DriverViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)


    # drivers
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class InvoicesViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)


    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
        
class ImagesViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)


    # drivers
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class VehiclesViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)


    # drivers
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer

class VehicleDamagesViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)


    # drivers
    queryset = VehicleDamages.objects.all()
    serializer_class = VehicleDamagesSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)

    # schedule
    queryset = ScheduledDate.objects.all()
    serializer_class = ScheduledDatesSerializer

class DataViewSet(APIView):
    # Authentication
    permission_classes = (IsAuthenticated,)
   

    # function for all data
    def get(self, request):
        ## defining overall data objects
        drivers = Driver.objects.all()
        schedule = ScheduledDate.objects.all()
        images = Images.objects.all()
        vehicles = Vehicles.objects.all()
        deductions = DeductionType.objects.all()
        support = SupportType.objects.all()

        content = {
            'data': returnOrderdData(drivers, schedule, images, vehicles, deductions, support)
        }
        return Response(content)

class StatisticsViewSet(APIView):
    permission_classes = (IsAuthenticated,)
   

    def get(self, request):
        ## defining overall data objects
        drivers = Driver.objects.all()
        schedule = ScheduledDate.objects.all()
        images = Images.objects.all()

        content = {
            'data': statistics(schedule)
        }

        return Response(content)

class MapViewSet(APIView):
    # Authentication
    permission_classes = (IsAuthenticated,)
 
    # This route is just a route that allows us to call the function in the test_data.py file with the correct environment  

    # function for all data
    def get(self, request):
        content = {
            'data': importData(ScheduledDate, Driver, DriverManager, ScheduledDatesManager) # the function is actually called in this file... so it has this files scope.... why we put things in 
            # functions... makes them modular and then we can control their scope 
        }

        return Response(content)

class SupportViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)

    queryset = SupportType.objects.all()
    serializer_class = SupportTypeSerializer

class DeductionViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)

    queryset = DeductionType.objects.all()
    serializer_class = DeductionTypeSerializer

class VehicleScheduledDateViewSet(viewsets.ModelViewSet):
    # Authentication
    permission_classes = (IsAuthenticated,)

    queryset = VehicleScheduledDate.objects.all()
    serializer_class = VehicleScheduledDateSerializer

class VehicleMapViewSet(APIView):

    # Authentication
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        drivers = Driver.objects.all()
        vehicles = Vehicles.objects.all()
        vehiclesDates = VehicleScheduledDate.objects.all()
        images = Images.objects.all().order_by('driver_id')
        theDate = request.body

        content = {
            'data': returnVanOrderedData(vehicles, vehiclesDates, images, drivers, theDate)
        }
        return Response(content)   

        # function for all data
    def get(self, request):
        drivers = Driver.objects.all()
        vehicles = Vehicles.objects.all()
        vehiclesDates = VehicleScheduledDate.objects.all()
        images = Images.objects.all().order_by('driver_id')
        content = {
            'data': returnVanOrderedData(vehicles, vehiclesDates, images, drivers) # the function is actually called in this file... so it has this files scope.... why we put things in 
            # functions... makes them modular and then we can control their scope 
        }

        return Response(content)

class InvoiceViewSet(APIView):
    # function for all data
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        invoices = Invoice.objects.all()
        drivers = Driver.objects.all()
        schedule = ScheduledDate.objects.all().order_by('date')
        vehicles = Vehicles.objects.all()
        deductions = DeductionType.objects.all()
        support = SupportType.objects.all()
        theDate = request.body

        content = {
            'data': invoice(drivers, schedule, vehicles, deductions, support, theDate)
        }
        return Response(content)   

    def get(self, request):
        # defining overall data objects
        invoices = Invoice.objects.all()
        drivers = Driver.objects.all()
        schedule = ScheduledDate.objects.all()
        vehicles = Vehicles.objects.all()
        deductions = DeductionType.objects.all()
        support = SupportType.objects.all()

        content = {
            'data': invoice(drivers, schedule, vehicles, deductions, support)
        }
        return Response(content)

class DailyServiceViewSet(APIView):
    # function for all data
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        drivers = Driver.objects.all()
        schedule = ScheduledDate.objects.all().order_by('date')
        deductions = DeductionType.objects.all()
        support = SupportType.objects.all()
        theDate = request.body

        content = {
            'data': dailyService(drivers, schedule, deductions, support, theDate)
        }
        return Response(content)   

    def get(self, request):
        # defining overall data objects
        drivers = Driver.objects.all()
        schedule = ScheduledDate.objects.all().order_by('date')
        deductions = DeductionType.objects.all()
        support = SupportType.objects.all()

        content = {
            'data': dailyService(drivers, schedule, deductions, support)
        }
        return Response(content)        

class securityViewSet(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        managerList = managers.objects.all()

        return Response({
            'token': tokenizer(managerList, request.body)
        })

class ComplianceMapViewSet(APIView):
    
    # Authentication
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        drivers = Driver.objects.all()
        vehicles = Vehicles.objects.all()
        vehiclesDates = VehicleScheduledDate.objects.all().order_by('date')
        images = Images.objects.all().order_by('driver_id')
        theDate = request.body

        content = {
            'data': complianceCheck(vehicles, vehiclesDates, images, drivers, theDate)
        }
        return Response(content)   

        # function for all data
    def get(self, request):
        drivers = Driver.objects.all()
        vehicles = Vehicles.objects.all()
        vehiclesDates = VehicleScheduledDate.objects.all().order_by('date')
        images = Images.objects.all().order_by('driver_id')
        content = {
            'data': complianceCheck(vehicles, vehiclesDates, images, drivers) # the function is actually called in this file... so it has this files scope.... why we put things in 
            # functions... makes them modular and then we can control their scope 
        }

        return Response(content)

class AutoSchedulingMapViewSet(APIView):
    
    # Authentication
    permission_classes = (IsAuthenticated,)

    def post(self, request): 
        drivers = Driver.objects.all()
        schedule = ScheduledDate.objects.all().order_by('date')
        theDate = request.body

        content = {
            'data': addDatedDriver(drivers, schedule, theDate)
        }
        return Response(content)   

        # function for all data
    def get(self, request):
        drivers = Driver.objects.all()
        schedule = ScheduledDate.objects.all().order_by('date')
        content = {
            'data': addDatedDriver(drivers, schedule) # the function is actually called in this file... so it has this files scope.... why we put things in 
            # functions... makes them modular and then we can control their scope 
        }

        return Response(content)

class docDrivers(APIView):
    
    # Authentication
    permission_classes = (IsAuthenticated,) 

        # function for all data
    def get(self, request):
        drivers = Driver.objects.all()
        images = Images.objects.all().order_by('driver_id')
        content = {
            'data': documentsDriversOnly(drivers, images) # the function is actually called in this file... so it has this files scope.... why we put things in 
            # functions... makes them modular and then we can control their scope 
        }

        return Response(content)