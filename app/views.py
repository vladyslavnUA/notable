from rest_framework import viewsets, filters, status
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def appointment(request, uniqueID):
    try: 
        appointment = Appointment.objects.get(uniqueID=uniqueID) 
    except Appointment.DoesNotExist: 
        return JsonResponse({'message': 'The appointment does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        appointment_serializer = AppointmentSerializer(appointment) 
        return JsonResponse(appointment_serializer.data) 
 
    elif request.method == 'PUT': 
        appointment_data = JSONParser().parse(request) 
        appointment_serializer = AppointmentSerializer(appointment, data=appointment_data) 
        if appointment_serializer.is_valid(): 
            appointment_serializer.save() 
            return JsonResponse(appointment_serializer.data) 
        return JsonResponse(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        appointment.delete() 
        return JsonResponse({'message': 'Appointment was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

class AppointmentViewSet(viewsets.ModelViewSet):
    search_fields = ['date']
    filter_backends = [filters.SearchFilter]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def delete(self, pk):
        appointment = self.get_object(pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def delete(request, uniqueID):
    # print(uniqueID)
    try:
        found = Appointment.objects.filter(uniqueID=uniqueID)
        found.delete()
        return 'Appointment Deleted'
    except Appointment.DoesNotExist:
        return 'Appointment is not active'