from blog.models import Category, Article

def get_categories(request):
    
    used_categories = Article.objects.filter(public=True).values_list('categorys', flat=True)
    categories = Category.objects.filter(
        id__in=used_categories
    ).values_list(
        'id', 
        'name'
    )
    
    return {
        'categories': categories,
        'ids': used_categories
    }
