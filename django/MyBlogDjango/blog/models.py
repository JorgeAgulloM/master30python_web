from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100, verbose_name='Name')
    description=models.CharField(max_length=255, verbose_name='Description')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
        
    def __str__(self):
        return self.name
    
class Article(models.Model):
    title=models.CharField(max_length=150, verbose_name='Page title')
    content=RichTextField(verbose_name='Page content')
    image=models.ImageField(default='null', verbose_name='Image') 
    public=models.BooleanField(verbose_name='Is public?')
    user=models.ForeignKey(User, verbose_name='Created by user', on_delete=models.CASCADE)
    categorys=models.ManyToManyField(Category, verbose_name='Categorys', null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at=models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        verbose_name='Article'
        verbose_name_plural='Articles'
        
    def __str__(self) -> str:
        return self.title
    