from django.contrib.auth.models import User
from .models import Employee, ScheduledDate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, EmployeeSerializer, ScheduledDatesSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) 

    queryset = Employee.objects.all().order_by('name')
    serializer_class = EmployeeSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows employees to be viewed or edited
    """
    queryset = ScheduledDate.objects.all()
    serializer_class = ScheduledDatesSerializer

class CoolViewSet(APIView):
    permission_classes = (IsAuthenticated,)    

    def get(self, request):
        content = {
            'message': 'hello there'
        }
        return Response(content)

