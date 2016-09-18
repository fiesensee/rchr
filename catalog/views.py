from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Article, Newspaper, Catalog

# Create your views here.

def addArticle(request):

    positive = len(Article.objects.filter(judging='positive'))
    neutral = len(Article.objects.filter(judging='neutral'))
    negative = len(Article.objects.filter(judging='negative'))
    indecisive = len(Article.objects.filter(judging='indecisive'))
    catalog = Catalog.objects.first()
    activeNewspaper = catalog.activeNewspaper

    context = {
        'positive': positive,
        'neutral': neutral,
        'negative': negative,
        'indecisive': indecisive,
        'newspaper': activeNewspaper
    }

    if request.method == 'POST':
        newArticle = Article()
        newArticle.author = request.POST['author']
        newArticle.text = request.POST['text']
        newArticle.title = request.POST['title']
        newArticle.source = request.POST['source']
        newArticle.timestamp = request.POST['date']
        newArticle.judging = request.POST['judgement']
        newArticle.newspaper = activeNewspaper
        newArticle.save()

        return HttpResponseRedirect('/')
    return render(request, 'catalog/addArticle.html', context)

def changeNewspaper(request):
    if request.method == 'POST':
        newActive = Newspaper.objects.get(pk = request.POST['newspaper'])
        catalog = Catalog.objects.first()
        catalog.activeNewspaper = newActive
        catalog.save()

        return HttpResponseRedirect('/')
    newspapers = Newspaper.objects.all()
    context = {
        'newspapers': newspapers
    }
    return render(request, 'catalog/changeNewspaper.html', context)

def addNewspaper(request):

    if request.method == 'POST':
        newPaper = Newspaper()
        newPaper.name = request.POST['name']
        newPaper.save()
        return HttpResponseRedirect('/')

    return render(request, 'catalog/addNewspaper.html')
