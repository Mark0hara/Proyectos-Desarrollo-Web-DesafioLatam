from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import FormularioRegistro, FormularioArrendatario, FormularioArrendador
from .models import Arrendatario, Arrendador


# ============ VISTA DE REGISTRO (1.2) ============
def registro_view(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente
            return redirect('elegir_tipo_usuario')
    else:
        form = FormularioRegistro()
    return render(request, 'usuarios/registro.html', {'form': form})


# ============ VISTA PARA ELEGIR TIPO DE USUARIO ============
@login_required
def elegir_tipo_usuario_view(request):
    # Si ya tiene perfil, redirigir al perfil
    if hasattr(request.user, 'arrendatario') or hasattr(request.user, 'arrendador'):
        return redirect('perfil')
    return render(request, 'usuarios/elegir_tipo.html')


# ============ VISTA PARA CREAR PERFIL ============
@login_required
def crear_perfil_view(request, tipo):
    if request.method == 'POST':
        if tipo == 'arrendatario':
            form = FormularioArrendatario(request.POST)
            if form.is_valid():
                perfil = form.save(commit=False)
                perfil.user = request.user
                perfil.save()
                return redirect('perfil')
        elif tipo == 'arrendador':
            form = FormularioArrendador(request.POST)
            if form.is_valid():
                perfil = form.save(commit=False)
                perfil.user = request.user
                perfil.save()
                return redirect('perfil')
    else:
        if tipo == 'arrendatario':
            form = FormularioArrendatario()
        elif tipo == 'arrendador':
            form = FormularioArrendador()
        else:
            return redirect('elegir_tipo_usuario')
    
    return render(request, 'usuarios/crear_perfil.html', {'form': form, 'tipo': tipo})


# ============ VISTA DE PERFIL (1.4) ============
@login_required
def perfil_view(request):
    usuario = request.user
    
    
    if hasattr(usuario, 'arrendatario'):
        perfil = usuario.arrendatario
        tipo = 'Arrendatario'
        form = FormularioArrendatario(instance=perfil)
    elif hasattr(usuario, 'arrendador'):
        perfil = usuario.arrendador
        tipo = 'Arrendador'
        form = FormularioArrendador(instance=perfil)
    else:
        return redirect('elegir_tipo_usuario')
    
    
    if request.method == 'POST':
        if tipo == 'Arrendatario':
            form = FormularioArrendatario(request.POST, instance=perfil)
        else:
            form = FormularioArrendador(request.POST, instance=perfil)
        
        if form.is_valid():
            form.save()
            return redirect('perfil')
    
    context = {
        'usuario': usuario,
        'perfil': perfil,
        'tipo': tipo,
        'form': form
    }
    return render(request, 'usuarios/perfil.html', context)


# ============ VISTA DE LOGIN (1.1) ============
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('perfil')  # (1.3) Redirección
    return render(request, 'usuarios/login.html')


# ============ VISTA DE LOGOUT ============
def logout_view(request):
    logout(request)
    return redirect('login')