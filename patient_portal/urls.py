from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
]
