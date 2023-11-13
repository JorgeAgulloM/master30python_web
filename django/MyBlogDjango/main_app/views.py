from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    
    params = {
        'title': 'Index'
    }
    
    return render(request, 'main_app/index.html', params)

def about(request):
    
    params = {
        'title': 'About'
    }
    
    return render(request, 'main_app/about.html', params)

def register_page(request):
    
    register_form = UserCreationForm()
    
    if request.method=='POST':
        register_form = UserCreationForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            
            return redirect('index')
    
    params = {
        'title': 'Register',
        'register_form': register_form
    }
    
    return render(request, 'users/register.html', params)
