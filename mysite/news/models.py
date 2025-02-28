from django.db import models

from tinymce.models import HTMLField
from .helpers import *

# Create your models here.
class Category(models.Model):
    LAYOUT_CHOICE = (
        ('list', 'List'),
        ('gird', 'Gird')
    )
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    is_homepage = models.BooleanField(default=False)
    layout = models.CharField(max_length=10, choices=LAYOUT_CHOICE, default='list')
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    ordering = models.IntegerField(default=0)

    # return self.name, not return an object 
    def __str__(self):
        return self.name
        
class Article(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    special = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    ordering = models.IntegerField(default=0)
    published_at = models.DateTimeField()
    content = HTMLField(default='')
    # content = models.TextField(default='')
    image = models.ImageField(default='', upload_to=get_file_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
