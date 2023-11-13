from django.contrib import admin
from .models import Category, Article

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created_at',)
    search_fields = ('name', 'content') # Añade un buscador
    list_display = ('name', 'description', 'created_at')
    
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=('user', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username', 'categorys__name') # Añade un buscador
    list_filter = ('public', 'user__username', 'categorys__name') # Añade un filtro
    list_display = ('title', 'public', 'user', 'created_at')
    ordering = ('-created_at',)
    
    # Hook
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
