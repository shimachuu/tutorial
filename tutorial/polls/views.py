from django.shortcuts import render, HttpResponse, get_object_or_404
from django.utils.html import mark_safe

from .models import Question

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world! You're at the polls index.")
    '''return render(request, 'polls/index.html',{
        'hoge': 'test string',
        'fuga': '<br>tag<br>',
        'piyo': mark_safe('<br>tag<br>')
    })'''

    return render(request, 'polls/index.html', {
        'questions': Question.objects.all(),
    })

def detail(request, pk):
    #get_object_or_404の仕組みはよくわからん
    obj = get_object_or_404(Question, pk=pk)
    return render(request, 'polls/detail.html', {
        'question': Question.objects.get(pk=pk)
    })

