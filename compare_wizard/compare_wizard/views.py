from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'index.html')

def login(request):
  return render(request, 'accounts/login.html')

def community(request):
  return render(request, 'community.html')