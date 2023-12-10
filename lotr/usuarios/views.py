from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

def login_usuario(request):
    if request.method == "POST":
        username = request.POST["usuario"]
        password = request.POST["contrasena"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
      
        else:
            messages.success(request, ("Error al iniciar la sesion, vuelve a intentarlo"))
            return redirect('login')
        
    else:
        return render(request, 'auth/login.html', {})

def logout_usuario(request):
    logout(request)
    messages.success(request, ("LogOut exitoso"))
    return redirect('index')

def registrar_usuario(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data['username']
            contrasena1 = form.cleaned_data['password1']

            user = authenticate(username=usuario, password1=contrasena1)
            login(request, user)
            messages.success(request, ("Usuario registrado con exito"))
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    return render(request, 'auth/registrar.html', {'form': form})