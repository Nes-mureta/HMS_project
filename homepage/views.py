from django.shortcuts import render
from django.views.generic import TemplateView


# the homepage hosts links to all the other views

class HomepageView(TemplateView):
  template_name = 'homepage.html'

