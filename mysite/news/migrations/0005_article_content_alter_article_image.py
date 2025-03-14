# Generated by Django 5.1.6 on 2025-02-28 07:38

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
