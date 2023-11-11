from django.shortcuts import render, HttpResponse, redirect
from first_app.models import Article

# Create your views here.
# MVC = Model View Controller
# MVT = Model View Template (For Django)
# In Django the View is the Template and the Controller is the View

layout = """
    <h1>Web site with Django | by Jorge Agulló</h1>
    <hr/>
    <ul>
        <li>
            <a href='/index'>Index</a>
        </li>
        <li>
            <a href='/helloworld'>Hello World</a>
        </li>
        <li>
            <a href='/pagetest'>Page Test</a>
        </li>
        <li>
            <a href='/yearlist'>Year List</a>
        </li>
        <li>
            <a href='/contact'>Contact Page</a>
        </li>
    </ul>
    <hr/>
"""

def index(request):
    return render(request, 'index.html')

def hello_world(request):
    return render(request, 'hello_world.html')
    
def page_test(request, redirection:int=0):
    
    if redirection == 1:
        return redirect('index')
    elif redirection == 2:
        return redirect('contact', name='Jorge', surname='Agulló')
    
    params = {
        'text': '',
        'list': [1, 2, 3, 4, 5, 6]    
    }
    
    return render(request, 'page_test.html', params)
    
def year_list(request):

    year = 2021
    years = []
    while year <= 2050:
        years.append(str(year)) 
        year += 1
    
    params = {
        'name': 'Jorge',
        'title': 'Year List',
        'my_var': 'I am a variable, i`m on the view',
        'years' : years
    }    
    
    return render(request, 'year_list.html', params)
    
def contact(request, name:str='', surname:str=''):
    welcome = 'Introduce nombre/apellido en la url'
    
    if name and surname:
        welcome = f'Hello {name} {surname}, how are you?'
    elif name:
        welcome = f'<h3>Hello {name}, how are you?</h3>'
        
    params = {
        'title': 'Contact page',
        'welcome': welcome,
        'creator': 'Created by Jorge Agulló'
    }
        
    return render(request, 'contact.html', params)

def create_article(request, title:str, content:str, public:str):
    new = Article(
        title=title,
        content=content,
        public=bool(public)
    )
    new.save()
    
    return HttpResponse(f'Created article: {new.title} - {new.content}')

def get_article(request, title:str):
    
    try:
        get = Article.objects.get(title=title)
    except Exception as e:
        HttpResponse(f'Error: {e}')
    
    return HttpResponse(f'Articulo: {get.title} - {get.content}')

def get_articles(request):
     
    try:
        # Se puede usar order_by() en vez de all(), order_by('id'), order_by('-id') `inverso` 
        # Se puede limitar la consulta usando las opciones de segregación de las listas, como [:3]
        # Se puede usar filtrado
        # articles = Article.objects.filter(title='My title', id=1)
        # Se pueden usar los llamados ````lookups````
        # Similar a like para sql -> `title__contains`
        # articles = Article.objects.filter(title__contains='My')
        # Exact -> `title__exact`: key sensitive
        # articles = Article.objects.filter(title__exact='My') 
        # IExact -> `title__iexact`: no key sensitive
        # articles = Article.objects.filter(title__exact='My')
        # gt (Graded than) -> `id__gt`: no key sensitive
        # articles = Article.objects.filter(id__gt=10)
        # gte (Graded than or equal) -> `id__gte`: no key sensitive
        # articles = Article.objects.filter(id__gte=10)
        # lt (less than) -> `id__lt`: no key sensitive
        # articles = Article.objects.filter(id__lt=10)
        # lte (less than or equal) -> `id__lte`: no key sensitive
        # articles = Article.objects.filter(id__lte=10)
        # Son combinables...
        
        articles = Article.objects.all()    
                
    except Exception as e:
        HttpResponse(f'Error: {e}')      

    params = {
        'title': 'Articles',
        'articles': articles
    }

    return render(request, 'articles.html', params)

def update_article(request, id:int):
    
    try:
        
        update = Article.objects.get(pk=id)
        
        update.title='My old title'
        update.content='My old content'
        update.public=True
        
        update.save()
        
        get = Article.objects.get(pk=id)
        
    except Exception as e:
        HttpResponse(f'Error: {e}')
        
    return HttpResponse(f'Update Article: {get.title} - {get.content}')

def delete_article(request, id):
    try:
        deleted = Article.objects.get(pk=id)
        deleted.delete()
    except Exception as e:
        HttpResponse(f'Error: {e}')
        
    return redirect('articles')