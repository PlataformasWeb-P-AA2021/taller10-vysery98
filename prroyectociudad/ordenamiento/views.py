from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
# Clases - models.py
from ordenamiento.models import *
# Formularios - forms.py
from ordenamiento.forms import *

# Create your views here.

# Obtención de los registros desde la BD
def index(request):
    parroquias = Parroquia.objects.all()
    barrios = Barrio.objects.all()
    informacion_template = {'parroquias': parroquias, 'numParroquias': len(parroquias), 'barrios': barrios, 'numBarrios': len(barrios)}
    return render(request, 'index.html', informacion_template)

# Visualizar Data
def getParroquia(request, id): 
    parroquias = Parroquia.objects.get(pk=id)  
    informacion_template = {'parroquias': parroquias}
    return render(request, 'getParroquia.html', informacion_template)

# Crear data
def setParroquia(request):
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}
    return render(request, 'setParroquia.html', diccionario)

def setBarrioParroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioParroquiaForm(parroquia, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioParroquiaForm(parroquia)
    diccionario = {'formulario': formulario, 'parroquia': parroquia}

    return render(request, 'setBarrioParroquia.html', diccionario) 

def setBarrio(request):
    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'setBarrio.html', diccionario)

# Editar data
def editParroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario, 'parroquia': parroquia}

    return render(request, 'editParroquia.html', diccionario) 
    
def editBarrio(request, id):
    barrio =Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario,'barrio': barrio}

    return render(request, 'editBarrio.html', diccionario) 
