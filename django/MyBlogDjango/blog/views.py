from django.shortcuts import render

# Create your views here.

def articles(request):
    
    
    params = {
        'title': 'Articles'
    }
    
    return render(request, 'articles/list.html', params)
