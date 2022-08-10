from django.shortcuts import render, redirect

# Create your views here.
# def workspace(request):
#   return render(request, 'workspace.html')

# def community(request):
#   return render(request, 'community.html')

def project(request):
  return render(request, 'project.html')

def dashboard(request):
  return render(request, 'main.html')