from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# RichTextField. Este componente pertenece a ckeditor, es configurable, buscar en google.
# https://django-ckeditor.readthedocs.io/en/latest/
# https://ckeditor.com/latest/samples/toolbarconfigurator/#basic


class Page(models.Model):
    title=models.CharField(max_length=50, verbose_name='Page title')
    content=RichTextField(verbose_name='Page content') 
    slug=models.CharField(unique=True, max_length=50, verbose_name='URL Friendly')
    order=models.IntegerField(default=0, verbose_name='Order pages')
    visible=models.BooleanField(verbose_name='Is visible?')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at=models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        verbose_name='Page'
        verbose_name_plural='Pages'
        
    def __str__(self) -> str:
        return self.title
