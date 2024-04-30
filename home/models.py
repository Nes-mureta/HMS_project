from django.db import models

class HomePage(models.Model):
    logo = models.CharField(max_length=360)
   
    def __str__(self):
        return self.logo