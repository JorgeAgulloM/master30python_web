from django.db import models

# Create your models here.

class Page(models.Model):
    title=models.CharField(max_length=50, verbose_name='Page title')
    content=models.TextField(verbose_name='Page content')
    slug=models.CharField(unique=True, max_length=50, verbose_name='URL Friendly')
    visible=models.BooleanField(verbose_name='Is visible?')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at=models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        verbose_name='Page'
        verbose_name_plural='Pages'
        
        def __str__(self) -> str:
            return self.title
