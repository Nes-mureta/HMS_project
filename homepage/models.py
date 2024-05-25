from django.db import models
from django.contrib.auth.models import User 

# the doctors models

class DoctorRequest(models.Model):
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  request_date=models.DateTimeField(auto_now_add=True)
  status=models.CharField (
    max_length=10, choices=[('pending','pending'), ('accepted','accepted'),('rejaected', 'rejected')], default='pending'
  )
  gender=models.CharField(max_length=10, choices=[('male','male'), ('female','female'),('others','others')], null=False)
  field_of_operation=models.CharField(max_length=50, null=False)