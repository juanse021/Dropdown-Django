from django.shortcuts import render
from django.core import serializers
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_protect
from . models import Marca, Modelo, AlmacenCarro
from django.http import JsonResponse


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
    marca = Marca.objects.all()
    info = request.GET.get('info')

    print("info {}". format(info))
    #mar = request.GET.get('marca_id')
    #mod = request.GET.get('modelo')

    context = {
        'marca': marca
    }

    #print("marca:{}, modelo:{}".format(mar, mod))

    return render(request, 'almacen_comprar.html', context)

def modelos_json(request):
    modelo_json = serializers.serialize("json", Modelo.objects.all())
    return HttpResponse(modelo_json, content_type="application/json")

