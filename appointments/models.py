from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from .utils import is_doctor_available_at



class Doctor(models.Model):
  
  avilable_for=models.BooleanField(default=True)
  
  id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=100)
  speciality=models.CharField(max_length=100)
  
  def is_available_at(self,time):
    return True
  
  def get_schedule(self):
    appointments=Appointment.objects.filter(doctor=self)
    schedule=[( appointment.date, appointment.time, appointment.status ) for appointment in appointments]
    return schedule
    
  
  
class Patient(models.Model):
  id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=100)
  age=models.IntegerField()
  gender=models.CharField(max_length=10)
  
  

class Appointment(models.Model):
  id=models.AutoField(primary_key=True)
  doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
  patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
  disease=models.CharField(max_length=100)
  date=models.DateTimeField()
  time=models.TimeField()
  status=models.CharField(max_length=100)
  
  def clean(self):
    if  is_doctor_available_at(self.doctor, self.time)==False:

        raise ValidationError("Doctor is not available on this date and time")

  class meta:
    unique_together=('doctor','time')
  

  def get_absolute_url(self):
    return reverse('appointment', kwargs={'pk': self.pk})
  