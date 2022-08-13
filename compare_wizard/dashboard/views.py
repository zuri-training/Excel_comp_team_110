from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Project#, DocFile

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

    # instances = Project.objects.all().filter(user = user)
    
    context = {'title': title}

  return render(request, 'main.html', context)# redirect


def del_fxn(request, pj_id):
  instance = Project.objects.get(id=pj_id)
  instance.delete()

  return redirect(project)


def down_fxn(request, pj_id):
  instance = Project.objects.get(id=pj_id)
  
  return instance.file.url


# def userData(request, title):
#   user = User.objects.get(id = request.user.id)
#   project = Project.objects.get(project_name=title)

#   if DocFile.objects.filter(project=project).exists():
#     return project
#   else:
#     instant = DocFile.objects.create(project=project)
#     instant.save()

#   return project


# def save1(request):
#   project = userData(request)
#   instance = DocFile.objects.get(project=project)
#   if request.method == 'POST':
#     instance.file_one = request.FILES['excel_file1']

#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
# {% url 'save2' %}

# def save2(request):
#   project = userData(request)
#   instance = DocFile.objects.get(project=project)
#   if request.method == 'POST':
#     instance.file_one = request.FILES['excel_file2']

#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
  