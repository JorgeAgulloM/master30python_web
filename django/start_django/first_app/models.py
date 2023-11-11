from django.db import models

# Create your models here.

class Aricle(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    public=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    creted_at=models.DateField()