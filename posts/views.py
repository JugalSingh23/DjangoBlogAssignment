from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.http import Http404

def home(request):
    articles = Article.objects.all()  
    context = {
        'articles': articles,  
    }
    return render(request, 'posts/home.html', context)

def article_detail(request,pk):
    article = Article.objects.get(pk=pk)

    if article:
        context = {'article':article}
        return render(request, 'posts/article_detail.html',context)
    else:
        raise Http404("Article does not exist")
        
    
