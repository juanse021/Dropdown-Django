import json
from django.shortcuts import render
from django.core import serializers
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.decorators.csrf import csrf_protect
from . models import Marca, Modelo, AlmacenCarro

# Create your views here.

class AlmacenCarroListView(ListView):
    model = AlmacenCarro
    template_name = 'almacen_listar.html'

class AlmacenCarroUpdate(UpdateView):
    model = AlmacenCarro
    success_url = reverse_lazy('concesionario:lista-carros')
    template_name = 'almacen_actualizar.html'
    fields = ['precio', 'cantidad']


def comprar_carro(request):
    marca_all = Marca.objects.all()

    mar = request.GET.get('marca', '')
    mod = request.GET.get('modelo_seleccionado', '')

    print("marca: ".format(mar))
    print("mod: ".format(mod))

    context = {
        'marca_all': marca_all
    }

    return render(request, 'almacen_comprar.html', context)

def modelos_json(request):
    id_marca = request.GET.get('id_marca', '')
    modelo_json = serializers.serialize("json", Modelo.objects.filter(marca=id_marca))
    return HttpResponse(modelo_json, content_type="application/json")
    
        


