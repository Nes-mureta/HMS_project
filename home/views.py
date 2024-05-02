from django.shortcuts import render,redirect
from django.views.generic import  TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView 

# Reuse existing methods and redirect to login page on successful registration

def register (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
       form=UserCreationForm()
    return render(request, 'register.html', {'form':form})
    


    

 