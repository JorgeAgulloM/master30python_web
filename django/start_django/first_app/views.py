from django.shortcuts import render, HttpResponse

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
            <a href='/contact/name/surname'>Contact Page</a>
        </li>
    </ul>
    <hr/>
"""

def index(request):
    return HttpResponse(layout+"""
        <h1>Index</h1>                    
    """)

def hello_world(request):
    return HttpResponse(layout+"""
        <h1>Hello World Form Django</h1>
        <h3> I am Jorge Agulló</h3>                    
    """)
    
def page_test(request):
    return HttpResponse(layout+"""
        <h1>My web page</h1>                   
        <h3>Created by Jorge Agulló</h3>                   
    """)
    
def year_list(request):
    html = """
        <p>Pair years list to 2050:</p>
        <ul>
    """
    year = 2021
    while year <= 2050:
        if year % 2 == 0:
            html += f'<li>{str(year)}</li>'
        year += 1
         
    html += '</ul>'
    
    return HttpResponse(layout+html)

    
def contact(request, name, surname):
    return HttpResponse(layout + f"""
        <h1>Contact page</h1>                   
        <h1>Hello {name} {surname}, how are you?</h1>                   
        <h3>Created by Jorge Agulló</h3>                   
    """)
