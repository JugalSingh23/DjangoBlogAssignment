# Generated by Django 5.0.7 on 2024-07-10 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='article_title',
            new_name='article_titl',
        ),
    ]
