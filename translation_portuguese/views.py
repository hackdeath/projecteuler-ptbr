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
        return HttpResponseRedirect(reverse('archives'))

    template = loader.get_template('translation_portuguese/archives.html')
    context = {
        'title': titulo,
        'quantidade_problemas': quantidade_problemas, 
        'index_list': lista_de_indices,
        'problems': problemas
    }

    return HttpResponse(template.render(context, request))

def problem(request, id):
    template = loader.get_template('translation_portuguese/index.html')
    context = {'title': 'Sobre - Project Euler'}

    return HttpResponse(template.render(context, request))
