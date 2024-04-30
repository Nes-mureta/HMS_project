"""
URL configuration for HMS_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from appointments import views

urlpatterns = [
    path('', include('home.urls')),
    
    path('admin/', admin.site.urls),
    
    path('doctors/<int:pk>/', views.DoctorListView.as_view(), name='doctors_list'),
    
    path('appointments/<int:pk>/', views.appointmentsListView.as_view(), name='appointments_list'),
    
    path('patients/<int:pk>/', views.patientsListView.as_view(), name='patients_list'),
        
    
    path('appointments/new/', views.appointmentCreateView.as_view(), name='book_appoointment'), 
    
    path('appointments/<int:pk>/', views.AppointmentsDetailView.as_view(), name='appointment'),
    
    path('appointments/<int:pk>/', views.AppointmentsDetailView.as_view(), name='appointment_detail'),
]
  
""" 
    path('appointments/<int:pk>/', views.appointmentsDetailView.as_view(), name='appointments_detail'),
    
    """