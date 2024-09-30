# projects/views.py

from django.shortcuts import render
from projects.models import Project

def project_index(request):
    # Perform a retrieve query on our database.
    projects = Project.objects.all()
    # Define a dictionary context with only one KV pair where value is all the projects we retrieved.
    context = {
        "projects": projects
    }
    # Passing the context dictionary as an argument to the template.
    return render(request, "projects/project_index.html", context)

def project_detail(request, pk):
    # Perform a retrieve query which retrieves the project with primary key, pk, equal to functions argument.
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)