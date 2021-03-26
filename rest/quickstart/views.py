from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest.quickstart.serializers import UserSerializer, GroupSerializer
from django.views.generic import DetailView, ListView
from .models import Shop, Sensor, SensorData
from django.http import HttpResponse


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class SensorDetailView(ListView):
    """
        Sensor detail view.
    """
    template_name = 'quickstart/sensor.html'
    #model = SensorData
    queryset = SensorData.objects.filter(location__isnull=False)


def homePageView(request):
    return HttpResponse('Hello, World!')

#https://stackoverflow.com/questions/23154525/django-generic-detail-view-must-be-called-with-either-an-object-pk-or-a-slug