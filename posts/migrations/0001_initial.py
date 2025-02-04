# Generated by Django 5.0.7 on 2024-07-10 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200)),
                ('article_content', models.TextField()),
                ('article_cover', models.ImageField(upload_to='article_covers/')),
            ],
        ),
    ]
