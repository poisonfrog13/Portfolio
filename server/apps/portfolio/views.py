from re import template
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from server.apps.portfolio.models import Project, Skill

def index(request, project_pk):
    
    # for projects
    project = get_object_or_404(Project, pk=project_pk)

    template = loader.get_template('index.html')
    context = {'project': project, }
    return render(request, 'index.html', context)