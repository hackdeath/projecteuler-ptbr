from django.http      import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template  import loader
from django.urls      import reverse
from .models          import Question
import math

def index(request):
    template = loader.get_template('translation_portuguese/index.html')
    context = {'title': 'Sobre - Project Euler'}

    return HttpResponse(template.render(context, request))

def archives(request, page = 1):
    page = int(page)
    amount_problems = Question.objects.count()
    problems_per_page = 50

    index_list = range(1, math.ceil(amount_problems / problems_per_page) + 1)
    title = 'Problemas arquivados - Project Euler'

    last = page * problems_per_page # last problem of this page
    first = last - problems_per_page # first problem of this page
    
    problems = Question.objects.filter(number__range=(first, last))

    if (not problems):
        return HttpResponseRedirect(reverse('archives_empty'))

    template = loader.get_template('translation_portuguese/archives.html')
    context = {
        'title': title,
        'amount_problems': amount_problems, 
        'index_list': index_list,
        'problems': problems,
        'current_index': page
    }

    return HttpResponse(template.render(context, request))

def recents(request):
    title = 'Problemas recentes - Project Euler'    
    problems = Question.objects.all().order_by('-number')[:10][::-1]
    template = loader.get_template('translation_portuguese/recents.html')
    
    context = {
        'title': title,
        'problems': problems
    }

    return HttpResponse(template.render(context, request))

def problem(request, id):
    previous_problem = Question.objects.filter(number = (int(id) - 1)) 
    current_problem  = Question.objects.get(number = id)
    next_problem     = Question.objects.filter(number = (int(id) + 1))

    if (previous_problem):
        previous_problem = previous_problem[0]

    if (next_problem):
        next_problem = next_problem[0]

    template = loader.get_template('translation_portuguese/problem.html')

    context = {
        'title': 'Problem {0} - Project Euler'.format(id),
        'previous_problem': previous_problem,
        'current_problem': current_problem,
        'next_problem': next_problem
    }

    return HttpResponse(template.render(context, request))
