from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, addCustomersForm
from .models import Customer,Truck

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
    customers=Customer.objects.all()
    return render(request, 'customers.html', {'customers':customers})

def customerInfo(request,pk):
    if request.user.is_authenticated:
        #Look up record
        customerInfo=Customer.objects.get(id=pk)
        return render(request, 'customerInfo.html', {'customerInfo':customerInfo})
    else:
        messages.success(request, 'You must be logged in to view this page')
        return redirect('login')

def deleteCustomers(request,pk):
    if request.user.is_authenticated:
        deleteCustomer=Customer.objects.get(id=pk)
        deleteCustomer.delete()
        messages.success(request,'Customer successfully deleted')
        return redirect('customers')
    else:
        messages.success(request,'You must be logged in to view this page')
        return redirect('login')
    
def addCustomers(request):
    form=addCustomersForm(request.POST or None)
    if request.user.is_authenticated:
            if request.method == "POST":
                if form.is_valid():
                    addCustomers=form.save()
                    messages.success(request, "Customer successfully added")
                    return redirect('customers')
    return render(request, 'addCustomers.html', {'form':form})

def updateCustomers(request, pk):
    if request.user.is_authenticated:
        currentCustomer=Customer.objects.get(id=pk)
        form=addCustomersForm(request.POST or None, instance=currentCustomer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer has been updated')
            return redirect('customers')
        return render(request, 'updateCustomers.html', {'form':form})
    else:
        messages.success(request, 'You must be logged in to view this page')
        return redirect('login')
    
def trucks(request):
    trucks=Truck.objects.all()
    return render(request, 'trucks.html', {'trucks':trucks})