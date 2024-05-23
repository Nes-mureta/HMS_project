from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import appointment, message


def appointment_list (request):
  appointments=appointment.objects.filter(patient=request.User)
  return render (request, 'patient_portal/appointment_list.html', {'appointments':appointments})

def book_appointment(request):
  if request.method == 'POST':
    doctor_id=request.POST.get ('doctor')
    date=request.POST.get ('date')
    time=request.POST.get ('time')
    
    doctor=User.objects.get(id=doctor_id)
    appointment=appointment(patient=request.User, doctor=doctor, date=date, time=time)
    appointment.save()
    return redirect('appointment_list')
  else:
    doctors=User.objects.filter()
    return render (request, 'book_appointment.html', {'doctors':doctors})



""" def chat_panel (request):
 """  
