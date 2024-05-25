from django import forms
from .models import DoctorRequest
from django.contrib.auth.models import User

class DoctorRequestForm(forms.ModelForm):
  class Meta:
    model = DoctorRequest
    fields = ['user','field_of_operation', 'gender']
 