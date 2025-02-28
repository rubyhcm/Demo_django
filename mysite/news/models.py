from django.db import models

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
    