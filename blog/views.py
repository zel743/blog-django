from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html')

def loginPage(request):
    return render(request, 'login.html')

def registerPage(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'register.html', context)

def windows(request):
    return render(request, 'windows.html' )

def linux(request):
    return render(request, 'linux.html' )

def macos(request):
    return render(request, 'macos.html' )
