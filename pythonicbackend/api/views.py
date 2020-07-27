from .models import Driver, ScheduledDate, DriverManager, ScheduledDatesManager, Images, Vehicles, Invoice, managers, VehicleDamages, SupportType, DeductionType, VehicleScheduledDate
from rest_framework.response import Response
from rest_framework.views import APIView, View
from rest_framework import viewsets
from Crypto.Cipher import AES
import json
import base64
import Crypto
from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Util.Padding import unpad
from rest_framework.permissions import IsAuthenticated
from .serializers import managersSerializer, DriverSerializer, ScheduledDatesSerializer, ImagesSerializer, VehiclesSerializer, InvoiceSerializer, VehicleDamagesSerializer, SupportTypeSerializer, DeductionTypeSerializer, VehicleScheduledDateSerializer
from .functions import timeDifference, returnOrderdData, statistics, invoice, returnVanOrderedData
from .test_data import importData
import csv, io 


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
    queryset = Driver.objects.all().order_by('name')
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
    queryset = ScheduledDate.objects.all().order_by('driver_id')
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

        # function for all data
    def get(self, request):
        drivers = Driver.objects.all()
        vehicles = Vehicles.objects.all()
        vehiclesDates = VehicleScheduledDate.objects.all()
        images = Images.objects.all()
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
        schedule = ScheduledDate.objects.all()
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

class securityViewSet(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        message = '0bc13d5abbb956ab5ca8a63fd8406d02ec8845b42bd5731a00224f04aeabcac9'
        key = 'askjbiocsdjhb238467sdkjfvasdfqwe' # TODO change to something with more entropy



        # AES
        BLOCK_SIZE = 16
        IV = message[:BLOCK_SIZE]

        try:
            b64 = json.loads(message)
            print(b64)
            iv = b64decode(b64[IV])
            ct = b64decode(b64[message])
            cipher = AES.new(key, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(ct), AES.block_size)
            print("The message was: ", pt)
        except ValueError:
            print("Incorrect decryption")

        # def pad(data):
        #     length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
        #     return data + chr(length)*length

        # def unpad(data):
        #     return data[:data[-1]]

        # def encrypt(message, key):
        #     IV = Crypto.Random.new().read(BLOCK_SIZE)
        #     aes = AES.new(key, AES.MODE_CBC, IV)
        #     return base64.b64encode(IV + aes.encrypt(pad(message)))

        # def decrypt(encrypted, key):
        #     encrypted = base64.b64decode(encrypted)
        #     IV = encrypted[:BLOCK_SIZE]
        #     aes = AES.new(key, AES.MODE_CBC, IV)
        #     print(unpad(aes.decrypt(encrypted[BLOCK_SIZE:])))
        #     return unpad(aes.decrypt(encrypted[BLOCK_SIZE:]))

        # decrypt(message.encode("utf8"), key.encode("utf8"))

        return Response('get')

    def post(self, request): 
        print(request.body)
        return Response(request.body)