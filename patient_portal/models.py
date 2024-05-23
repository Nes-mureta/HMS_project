from django.db import models
from django.contrib.auth.models import User

#booking appointments

class appointment(models.Model):
  patient=models.ForeignKey(User, on_delete=models.CASCADE, related_name='appoitments')
  doctor=models.ForeignKey(User, on_delete=models.CASCADE,related_name='doctor_appointments')
  date=models.DateField()
  time=models.TimeField()


# chat pannel

class message(models.Model):
  sender=models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
  recipient=models.ForeignKey(User, on_delete=models.CASCADE, related_name='recieved_messages')
  content=models.TextField()
  timestamp=models.DateTimeField(auto_now_add=True)