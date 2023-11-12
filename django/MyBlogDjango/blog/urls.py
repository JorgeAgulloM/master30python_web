from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles, name='articles'),
    path('category/<int:category_id>', views.category, name='category'),
]