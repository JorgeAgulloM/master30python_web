from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Model View Controller
# MVT = Model View Template (For Django)
# In Django the View is the Template and the Controller is the View

def index(request):
    return HttpResponse("""
        <h1>Inicio<h1>                    
    """)


def hello_world(request):
    return HttpResponse("""
        <h1>Hello World Form Django<h1>
        <h3> I am Jorge Agulló<h3>                    
    """)
    
def page_test(request):
    return HttpResponse("""
        <h1>Pagina de mi web<h1>                   
        <h3>Created by Jorge Agulló<h3>                   
    """)
