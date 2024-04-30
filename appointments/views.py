from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView,DetailView,CreateView
from.models import Appointment, Doctor, Patient
from .forms import AppointmentForm


  
class DoctorListView(ListView):
    model=Doctor
    template_name='doctors_list.html'
    context_object_name='doctors'

class DoctorDetailView(DetailView):
    model=Doctor
    template_name='doctor_detail.html'
    context_object_name='doctor'
    
    
    
    
class appointmentsListView(ListView):
    model=Appointment
    template_name='appointments_list.html'
    context_object_name='appointments'
    
class AppointmentsDetailView(DetailView):
    model=Appointment
    template_name='appointments_detail.html'
    context_object_name='appointment'
    
    def get_template_names(self):
        return ['./appointments_detail.html']
 
class appointmentCreateView(CreateView):
    model = Appointment
    fields = ['doctor', 'patient', 'date', 'time']
    template_name = 'book_appointment.html'


def book_appointment(request):
    if request.method=='POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            appointment=form.save()
            return redirect('appointments_confirmation.id')
        else:
            form=AppointmentForm()
            
        return render(request,'book_appoteintment.html',{'form':form})
    else:
        return redirect('appointments_list.html')
    
    
  
class patientsListView(ListView):
    model=Patient
    template_name='patients_list.html'
    context_object_name='patients'
    
class patientsDetailView(DetailView):
    model=Patient
    template_name='patient_detail.html'
    context_object_name='patient'
    
    
  
    