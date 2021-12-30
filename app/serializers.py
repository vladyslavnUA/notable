from django.contrib.auth.models import User, Group
from rest_framework import serializers


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['name']


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['url', 'name']

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']