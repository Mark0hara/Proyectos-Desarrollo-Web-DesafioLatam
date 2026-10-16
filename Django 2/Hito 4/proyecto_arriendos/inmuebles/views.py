from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Inmueble
from .forms import FormularioInmueble

# ✅ DEBE EXISTIR ESTA FUNCIÓN
@login_required
def crear_inmueble_view(request):
    if not hasattr(request.user, 'arrendador'):
        return HttpResponseForbidden("Solo los arrendadores pueden crear inmuebles.")

    if request.method == 'POST':
        form = FormularioInmueble(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.arrendador = request.user.arrendador
            inmueble.save()
            return redirect('listar_inmuebles')
    else:
        form = FormularioInmueble()

    return render(request, 'inmuebles/crear_inmueble.html', {'form': form})


# ✅ Y TAMBIÉN ESTA
@login_required
def editar_inmueble_view(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    
    if inmueble.arrendador.user != request.user:
        return HttpResponseForbidden("No tienes permiso para editar este inmueble.")

    if request.method == 'POST':
        form = FormularioInmueble(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('listar_inmuebles')
    else:
        form = FormularioInmueble(instance=inmueble)

    return render(request, 'inmuebles/editar_inmueble.html', {'form': form, 'inmueble': inmueble})


# ✅ Y ESTA
@login_required
def eliminar_inmueble_view(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    
    if inmueble.arrendador.user != request.user:
        return HttpResponseForbidden("No tienes permiso para borrar este inmueble.")

    if request.method == 'POST':
        inmueble.delete()
        return redirect('listar_inmuebles')

    return render(request, 'inmuebles/confirmar_eliminar.html', {'inmueble': inmueble})


# ✅ Y FINALMENTE ESTA
def listar_inmuebles_view(request):
    inmuebles = Inmueble.objects.filter(disponible=True)

    region_filtro = request.GET.get('region', '')
    comuna_filtro = request.GET.get('comuna', '')

    if region_filtro:
        inmuebles = inmuebles.filter(region=region_filtro)
    if comuna_filtro:
        inmuebles = inmuebles.filter(comuna=comuna_filtro)

    regiones = Inmueble.objects.filter(disponible=True).values_list('region', flat=True).distinct().order_by('region')

    if region_filtro:
        comunas = Inmueble.objects.filter(
            disponible=True, 
            region=region_filtro
        ).values_list('comuna', flat=True).distinct().order_by('comuna')
    else:
        comunas = Inmueble.objects.filter(disponible=True).values_list('comuna', flat=True).distinct().order_by('comuna')

    context = {
        'inmuebles': inmuebles,
        'regiones': regiones,
        'comunas': comunas,
        'region_seleccionada': region_filtro,
        'comuna_seleccionada': comuna_filtro,
    }
    return render(request, 'inmuebles/listar_inmuebles.html', context)