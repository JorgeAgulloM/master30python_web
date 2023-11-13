from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Page
# Create your views here.

@login_required(login_url='login')
def page(request, slug:str):
    
    page = Page.objects.get(slug=slug)
    
    params = {
        'page': page
    }
    
    return render(request, 'pages/page.html', params)