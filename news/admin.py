from django.contrib import admin
from .models import Category, Region, News

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_display_links = ('title',)

@admin.register(Region)
class AdminRegion(admin.ModelAdmin):
    list_display = ('pk','title')

@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_at', 'is_published')
    list_display_links = ('title', 'pk')
    list_editable = ('is_published',)
    search_fields = ('title',)