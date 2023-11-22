from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def login_user(request):
    # Check to see if the user is logging in to the website
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('home')
        else:
            messages.success(request, "Wrong username/password")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')

def register_user(request):
    return render(request, 'register.html', {})

def customers(request):
    return render(request, 'customers.html', {})