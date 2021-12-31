from django.db import models

TYPES = (
    ('New Patient', 'New Patient'),
    ('Follow-up', 'Follow-up'),
)

class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    uniqueID = models.CharField(max_length=255)
    
    def __str__(self):
        return self.first_name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    uniqueID = models.CharField(max_length=255)
    type = models.CharField(max_length=35,
                  choices=TYPES,
                  default="Follow-up")
    date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.doctor.first_name