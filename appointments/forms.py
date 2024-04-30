from .models import Appointment, Doctor, Patient
from django import forms 

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['doctor','patient','disease','date','time','status']
        