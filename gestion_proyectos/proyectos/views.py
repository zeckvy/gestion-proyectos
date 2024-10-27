from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto, Tarea
from .forms import ProyectoForm

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos/lista_proyectos.html', {'proyectos': proyectos})

def detalle_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    return render(request, 'proyectos/detalle_proyecto.html', {'proyecto': proyecto})

def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'proyectos/crear_proyecto.html', {'form': form})

def eliminar_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    proyecto.delete()
    return redirect('lista_proyectos')