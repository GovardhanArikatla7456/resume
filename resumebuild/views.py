from django.shortcuts import render
from .models import Project

# Create your views here.
'''def index(request):
    return render(request, 'resumebuild/index.html')'''
def project_list(request):
    projects = Project.objects.all()  # Retrieve all projects
    return render(request, 'resumebuild/project_list.html', {'projects': projects})

def filter_projects(request):
    if request.method == 'POST':
        category = request.POST["category"]
        if category:
            projects = Project.objects.filter(category=category)
        else:
            projects = Project.objects.all()
        return render(request, 'resumebuild/project_list.html', {'projects': projects})
    else:
        return render(request, 'resumebuild/project_list.html')

def add_to_resume(request, project_id):
    project = Project.objects.get(pk=project_id)
    # Logic to add the selected project to the user's resume
    return render(request, 'resumebuild/resume.html', {'project': project})
