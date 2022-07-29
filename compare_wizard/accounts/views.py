from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth import message

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('')
        else:
            # Return an 'invalid login' error message.
            # message.success(request, "there was an error")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html', {})