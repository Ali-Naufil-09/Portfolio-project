from django.shortcuts import render
from .models import Project
from django.http import Http404

# Create your views here.

def home(request):
    projects=Project.objects.all()
    return render(request,'projects/home.html', {'projects':projects}) #projects/home.html means our folder in which home.html is present is projects.  {projects:projects} menan that we have created a variable named projects for calling any project in template like html files

def detail(request,project_id):
      try:
        p=Project.objects.get(id=project_id)
      except Project.DoesNotExist:
          raise Http404('Project not found')
      return render(request,'projects/detail.html',{'projects':p}) #projects/detail.html means our folder in which detail.html is present is projects
    