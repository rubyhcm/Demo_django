from django.contrib import admin

# Register your models here.

from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'ordering', 'is_homepage', 'layout')
    # Create links between slug and name
    # prepopulated_fields = {'slug': ('name',)}

    list_filter = ('status', 'is_homepage', 'layout', 'name')
    search_fields = ('name',)
    class Media:
        js = ('my_admin/js/jquery-3.6.0.min.js', 'my_admin/js/slugify.min.js', 'my_admin/js/general.js')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'ordering')
    # Create links between slug and name
    # prepopulated_fields = {'slug': ('name',)}

    list_filter = ('status', 'name')
    search_fields = ('name',)
    class Media:
        js = ('my_admin/js/jquery-3.6.0.min.js', 'my_admin/js/slugify.min.js', 'my_admin/js/general.js')

admin.site.register(Category, CategoryAdmin)

admin.site.register(Article, ArticleAdmin)
