# schoolapp/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm, CreateUserForm 
from .forms import  Units, Nominals
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'index.html')

def admission(request):
    return render(request, 'admission.html')

def loginPage(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request, 'username OR password is incorrect')
            
    context={}    
    return render(request, 'login.html',context)

def odel(request):
    return render(request, 'odel.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        
            return redirect('contact') 
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def about(request):
    return render(request, 'about.html')

def signup(request):
    form = CreateUserForm(request.POST)
    if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account was created successfully for' + user)
            return redirect('login')
    context={'form':form}
    return render(request, 'signup.html', context)


def success(request):
    return render(request, 'success.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def results(request):
    return render(request, 'results.html')

def units(request):
    if request.method == 'POST':
        form = Units(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'unit registered successfully')
            return redirect('units')  
    else:
        form = Units()
    
    return render(request, 'units.html', {'form': form})

def nominals(request):
    if request.method == 'POST':
        form = Nominals(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'nominals registered successfully')
            return redirect('nominals') 
    else:
        form = Nominals()
    
    return render(request, 'nominals.html', {'form': form})

from django.contrib.auth import logout

def logout(request):
    return render(request, 'login.html')

