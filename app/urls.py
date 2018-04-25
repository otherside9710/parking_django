


from django.conf.urls import url, include
from django.contrib import admin

import views

urlpatterns = [
	url('^clientes/findall/$', views.ClientesView.as_view()),
	url('^clientesvscredenciales/findall/$', views.ClientesVsCredencialesView.as_view()),
	url('^credenciales/findall/$', views.CredencialesView.as_view()),
	url('^facturas/findall/$', views.FacturasView.as_view()),
	url('^parqueo/findall/$', views.ParqueoView.as_view()),
	url('^parqueovsclientes/findall/$', views.ParqueoVsClientesView.as_view()),
	url('^roles/findall/$', views.RolesView.as_view()),
	url('^tarifas/findall/$', views.TarifasView.as_view()),
	url('^tpvehiculo/findall/$', views.TpVehiculoView.as_view()),
	url('^usuarios/findall/$', views.UsuariosView.as_view()),
	url('^usuariosvscredenciales/findall/$', views.UsuariosVsCredencialesView.as_view()),
	url('^vehiculos/findall/$', views.VehiculosView.as_view()),
	url('^vehiculosvsclientes/findall/$', views.VehiculosVsClientesView.as_view()),
	url('^vehiculosvsparqueo/findall/$', views.VehiculosVsParqueoView.as_view()),
	url('^zonas/findall/$', views.ZonasView.as_view()),
]
