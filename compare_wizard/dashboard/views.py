from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Project

# Create your views here.
# def workspace(request):
#   return render(request, 'workspace.html')

# def community(request):
#   return render(request, 'community.html')

def project(request):
  user = User.objects.get(id = request.user.id)
  instances = Project.objects.all().filter(user = user)
    
  context = {'wanten': instances}
  return render(request, 'project.html', context)

def dashboard(request):
  return render(request, 'main.html')


def new_project(request):
  if request.method == 'POST':
    title = request.POST['title']
    status = request.POST['status']
    if status == 'on': 
      status = True
    else: 
      status = False
    user = User.objects.get(id = request.user.id)

    instance = Project.objects.create(user = user, project_name = title, status=status)
    instance.save()

    instances = Project.objects.all().filter(user = user)
    
    context = {'wanten': instances}

  return render(request, 'project.html', context)# redirect