from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from blog.models import Category, Article
# Create your views here.

@login_required(login_url='login')
def articles(request):
    
    # Obtener articulos
    articles = Article.objects.all()
    
    # Paginar articulos
    paginator = Paginator(articles, 2)
    
    # Obtener número de página
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    
    params = {
        'title': 'Articles',
        'articles': page_articles,
    }
    
    return render(request, 'articles/list.html', params)

@login_required(login_url='login')
def article(request, article_id):
    
    article = get_object_or_404(Article, id=article_id)
    
    params = {
        'article': article,
    }
    
    return render(request, 'articles/detail.html', params)

@login_required(login_url='login')
def category(request, category_id):
    
    category = get_object_or_404(Category, id=category_id)
    
    articles = Article.objects.filter(categorys=category)
    
    paginator = Paginator(articles, 2)
    
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    
    params = {
        'title': 'Categories',
        'category': category,
        'articles': page_articles,
    }
    
    return render(request, 'categories/category.html', params)
