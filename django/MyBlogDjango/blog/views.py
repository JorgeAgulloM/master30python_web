from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article
# Create your views here.

def articles(request):
    
    articles = Article.objects.all()
    
    params = {
        'title': 'Articles',
        'articles': articles,
    }
    
    return render(request, 'articles/list.html', params)

def category(request, category_id):
    
    category = get_object_or_404(Category, id=category_id)
    
    params = {
        'title': 'Categories',
        'category': category
    }
    
    return render(request, 'categories/category.html', params)
