# Generated by Django 5.0.7 on 2024-07-10 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_article_title_articles_article_titl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='article_titl',
            new_name='article_title',
        ),
    ]
