from django.contrib.auth.models import User, Group
from .models import Employee, ScheduledDate
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, EmployeeSerializer, ScheduledDatesSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited
    """
    queryset = ScheduledDate.objects.all()
    serializer_class = ScheduledDatesSerializer

