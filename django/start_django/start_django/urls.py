"""
URL configuration for start_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Import my views
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('helloworld/', views.hello_world, name='hello_world'),
    path('pagetest/', views.page_test, name='page_test'),
    path('pagetest/<int:redirection>', views.page_test, name='page_test'),
    path('yearlist/', views.year_list, name='year_list'),
    path('contact/', views.contact, name='contact'),
    path('contact/<str:name>', views.contact, name='contact'),
    path('contact/<str:name>/<str:surname>', views.contact, name='contact'),
]
