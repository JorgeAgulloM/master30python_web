from django import template

register = template.Library()

@register.filter(name='greeting')
def greeting(value):
    
    #Aquí puedo meter la funcionalidad que necesite
    
    return f"<h1 style='background:green;color:white;'>Welcome, {value}</h1>"