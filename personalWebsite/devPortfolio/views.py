from django.shortcuts import render
from devPortfolio.models import Project
# Create your views here.
# sends the data to HTML templates

def cover(requests):
    return render(requests, 'index.html',{})

def resume(requests):
    return render(requests, 'resume.html',{})

def project_index(requests):
    projects= Project.objects.all() # performs a query 
    url= str(Project.image).replace('static', '')
    context = { #dictonary for projects to set information to templates
        'projects': projects, 'url':url
    }
    return render(requests, 'project_index.html', context)