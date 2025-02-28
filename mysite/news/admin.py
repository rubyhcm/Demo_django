from django.contrib import admin
from .define import *

# Register your models here.

from .models import Category, Article, Feed

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'ordering', 'is_homepage', 'layout')
    # Create links between slug and name
    # prepopulated_fields = {'slug': ('name',)}

    list_filter = ('status', 'is_homepage', 'layout', 'name')
    search_fields = ('name',)
    class Media:
        js = APP_STATIC_JS
        css = APP_STATIC_CSS

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'ordering')
    # Create links between slug and name
    # prepopulated_fields = {'slug': ('name',)}

    list_filter = ('status', 'name')
    search_fields = ('name',)
    class Media:
        js = APP_STATIC_JS
        css = APP_STATIC_CSS

class FeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'ordering')
    # Create links between slug and name
    # prepopulated_fields = {'slug': ('name',)}

    list_filter = ('status', 'name')
    search_fields = ('name',)
    class Media:
        js = APP_STATIC_JS
        css = APP_STATIC_CSS

admin.site.register(Category, CategoryAdmin)

admin.site.register(Article, ArticleAdmin)

admin.site.register(Feed, FeedAdmin)

admin.site.site_header = APP_SITE_HEADER
