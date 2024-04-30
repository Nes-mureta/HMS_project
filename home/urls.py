from django.urls import path
from .views import HomePageView
from . import views


urlpatterns=[
  path('home/', views.HomePageView.as_view(),name='home')
]