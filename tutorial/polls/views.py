from django.shortcuts import render, HttpResponse
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

