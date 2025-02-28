from django.db import models

from tinymce.models import HTMLField
from .helpers import *
from .custom_field import CustomBooleanField
from .define import *

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    # is_homepage = models.BooleanField(default=False)
    is_homepage = CustomBooleanField()
    layout = models.CharField(max_length=10, choices=APP_LAYOUT_CHOICE, default='list')
    status = models.CharField(max_length=10, choices=APP_STATUS_CHOICE, default='draft')
    ordering = models.IntegerField(default=0)

    # return self.name, not return an object 
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Category'
        
class Article(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    # special = models.BooleanField(default=False)
    special = CustomBooleanField()
    status = models.CharField(max_length=10, choices=APP_STATUS_CHOICE, default='draft')
    ordering = models.IntegerField(default=0)
    published_at = models.DateTimeField()
    content = HTMLField(default='')
    # content = models.TextField(default='')
    image = models.ImageField(default='', upload_to=get_file_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Feed(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.CharField(max_length=10, choices=APP_STATUS_CHOICE, default='draft')
    ordering = models.IntegerField(default=0)
    link = models.CharField(max_length=250)

    def __str__(self):
        return self.name
