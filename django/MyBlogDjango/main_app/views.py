from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

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
    
    register_form = RegisterForm
    
    if request.method=='POST':
        register_form = RegisterForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Has been successfully registered')
            
            return redirect('index')
    
    params = {
        'title': 'Register',
        'register_form': register_form
    }
    
    return render(request, 'users/register.html', params)

def login_page(request):
    
    params = {'title': 'Login'}
    
    return render(request, 'users/login.html', params)
