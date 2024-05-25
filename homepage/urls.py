from django.urls import path
from . import views

urlpatterns =[
  path('homepage/', views.HomepageView.as_view(template_name='homepage.html'),name='homepage'),
  
  path('doctor_request/', views.submit_doctor_request, name='submit_doctor_request'),
]