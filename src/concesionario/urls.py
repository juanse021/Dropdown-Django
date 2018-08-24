from django.urls import path
from concesionario.views import AlmacenCarroListView, AlmacenCarroUpdate
from . import views

app_name = "concesionario"

urlpatterns = [
	path('comprar/', views.comprar_carro, name='comprar-carro'),
    path('actualizar/<int:pk>', AlmacenCarroUpdate.as_view(), name='actualizar-carros'),
    path('listar/', AlmacenCarroListView.as_view(), name='lista-carros'),
    path('comprar/json/', views.modelos_json, name='json-comprar-carros')    
]