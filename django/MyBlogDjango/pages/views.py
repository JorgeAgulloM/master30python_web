from django.shortcuts import render
from .models import Page
# Create your views here.

def page(request, slug:str):
    
    page = Page.objects.get(slug=slug)
    
    params = {
        'page': page
    }
    
    return render(request, 'pages/page.html', params)