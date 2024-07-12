from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import strip_tags

class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_content = RichTextField()
    article_cover = models.ImageField(upload_to='posts/static/images/article_covers/',blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    article_cover_text = models.CharField(max_length=94)


    def __str__(self):
        return self.article_title