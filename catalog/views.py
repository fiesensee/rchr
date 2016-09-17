from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Article, Newspaper

# Create your views here.

def addArticle(request):

    positive = len(Article.objects.filter(judging='positive'))
    neutral = len(Article.objects.filter(judging='neutral'))
    negative = len(Article.objects.filter(judging='negative'))
    indecisive = len(Article.objects.filter(judging='indecisive'))
    newspapers = Newspaper.objects.all()

    context = {
        'positive': positive,
        'neutral': neutral,
        'negative': negative,
        'indecisive': indecisive,
        'newspapers': newspapers
    }

    if request.method == 'POST':
        newArticle = Article()
        newArticle.author = request.POST['author']
        newArticle.newspaper = Newspaper.objects.get(pk = request.POST['newspaper'])
        newArticle.text = request.POST['text']
        newArticle.title = request.POST['title']
        newArticle.source = request.POST['source']
        newArticle.timestamp = request.POST['date']
        newArticle.judging = request.POST['judgement']
        newArticle.save()

        return HttpResponseRedirect('/')
    return render(request, 'catalog/addArticle.html', context)

def addNewspaper(request):

    if request.method == 'POST':
        newPaper = Newspaper()
        newPaper.name = request.POST['name']
        newPaper.save()
        return HttpResponseRedirect('/')

    return render(request, 'catalog/addNewspaper.html')
