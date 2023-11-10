from django.shortcuts import render, HttpResponse, redirect

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
    
    return render(request, 'page_test.html')
    
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
    html = '<h3>Introduce nombre/apellido en la url</h3>'
    
    if name and surname:
        html = f'<h3>Hello {name} {surname}, how are you?</h3>'
    elif name:
        html = f'<h3>Hello {name}, how are you?</h3>'
        
    return HttpResponse(layout + f"""
        <h1>Contact page</h1>                   
        {html}                   
        <h5>Created by Jorge Agulló</h5>
    """)
