from django.http      import HttpResponse
from django.shortcuts import render
from django.template  import loader

def index(request):
    template = loader.get_template('translation_portuguese/index.html')
    context = {'title': 'Sobre - Project Euler'}

    return HttpResponse(template.render(context, request))

def archives(request, pagina=1):
    index_list = range(1, 13)
    template = loader.get_template('translation_portuguese/archives.html')
    context = {
        'title': 'Problemas arquivados - Project Euler',
        'quantidade_problemas': 13,
        'index_list': index_list
    }

    return HttpResponse(template.render(context, request))
