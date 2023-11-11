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
