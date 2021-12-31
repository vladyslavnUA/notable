from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['uniqueID', 'first_name', 'last_name']

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['doctor', 'uniqueID', 'first_name', 'last_name', 'date', 'type']

class FindSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date']