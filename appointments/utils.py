def is_doctor_available_at(self,time):
  from .models import Appointment
  appointments=Appointment.objects.filter(doctor=self, time=time)
  if appointments.exists():
    return False
  return True
  