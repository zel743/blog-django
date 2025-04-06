from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha registrado tu usuario!')

            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'register.html', {'form': form})

def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Usa .get() para evitar el error
        password = request.POST.get('password')
        
        if not username or not password:
            messages.error(request, 'Por favor ingresa usuario y contraseña')
            return redirect('login')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.username}!') 
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'login.html')

def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Hasta pronto!')

    return redirect('login')
