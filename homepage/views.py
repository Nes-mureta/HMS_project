from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from.forms import DoctorRequestForm
from.models import DoctorRequest
from django.contrib import admin

# the homepage hosts links to all the other views

class HomepageView(TemplateView):
  template_name = 'homepage.html'


# the  doctor views

# user request to be a doctor

def submit_doctor_request(request):
  if request.method == 'POST':
      form = DoctorRequestForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('homepage')
  else:
      form = DoctorRequestForm()
  return render(request, 'doctor_request_form.html',  {'form': form})

# admin accepts or rejects doctors requests

class DoctorRequestAdmin(admin.ModelAdmin):
  list_display = ('user','request_date', 'field_of_operation', 'status')
  list_filter = ('request_date','status')
  actions=['accept_request', 'reject_request']
  
  
  def accept_request(self, request, queryset):
    queryset.update(status='accepted')
    if request.user.is_authenticated:
      return redirect('homepage',)
  accept_request.short_description='Accept request'
    
  def reject_request(self, request, queryset):
    queryset.update(status='rejected')
admin.site.register(DoctorRequest, DoctorRequestAdmin)

