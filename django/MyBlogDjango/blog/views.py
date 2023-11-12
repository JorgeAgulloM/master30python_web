from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Category, Article
# Create your views here.

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

def article(request, article_id):
    
    article = get_object_or_404(Article, id=article_id)
    
    params = {
        'article': article,
    }
    
    return render(request, 'articles/detail.html', params)

def category(request, category_id):
    
    category = get_object_or_404(Category, id=category_id)
    
    params = {
        'title': 'Categories',
        'category': category
    }
    
    return render(request, 'categories/category.html', params)
