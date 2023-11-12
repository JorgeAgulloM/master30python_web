from django.shortcuts import render

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
