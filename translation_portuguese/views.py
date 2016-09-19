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

def archives(request, pagina = 1):
    pagina = int(pagina)
    quantidade_problemas = Question.objects.count()
    problemas_por_pagina = 50

    lista_de_indices = range(1, math.ceil(quantidade_problemas / problemas_por_pagina) + 1)
    titulo = 'Problemas arquivados - Project Euler'

    ultimo = pagina * problemas_por_pagina
    primeiro = ultimo - problemas_por_pagina
    
    problemas = Question.objects.filter(number__range=(primeiro, ultimo))

    if (not problemas):
        return HttpResponseRedirect(reverse('archives_empty'))

    template = loader.get_template('translation_portuguese/archives.html')
    context = {
        'title': titulo,
        'quantidade_problemas': quantidade_problemas, 
        'index_list': lista_de_indices,
        'problems': problemas,
        'current_index': pagina
    }

    return HttpResponse(template.render(context, request))

def recents(request):
    titulo = 'Problemas recentes - Project Euler'
    
    problemas = Question.objects.all().order_by('-number')[:10]

    template = loader.get_template('translation_portuguese/recents.html')
    context = {
        'title': titulo,
        'problems': problemas
    }

    return HttpResponse(template.render(context, request))

def problem(request, id):
    problema = Question.objects.get(number = id)

    template = loader.get_template('translation_portuguese/problem.html')
    context = {
        'title': 'Problem {0} - Project Euler'.format(id),
        'problema': problema
    }

    return HttpResponse(template.render(context, request))
