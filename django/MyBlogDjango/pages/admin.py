from django.contrib import admin
from .models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at',)

admin.site.register(Page, PageAdmin)

# Configuration
title='Blog with django'
subtitle='Managment Panel'
admin.site.site_header=title
admin.site.site_title=title
admin.site.index_title=subtitle