# Generated by Django 5.1.6 on 2025-02-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_article_content_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='', upload_to='news/images/article/'),
        ),
    ]
