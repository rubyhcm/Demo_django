from django.contrib import admin

# Register your models here.

from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'ordering', 'is_homepage', 'layout')
    # Create links between slug and name
    # prepopulated_fields = {'slug': ('name',)}

    list_filter = ('status', 'ordering', 'is_homepage', 'layout')
    search_fields = ('name',)
    class Media:
        js = ('my_admin/js/jquery-3.6.0.min.js', 'my_admin/js/slugify.min.js', 'my_admin/js/general.js')

admin.site.register(Category, CategoryAdmin)
