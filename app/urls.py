from django.conf.urls import url, include
from django.contrib import admin

import views

urlpatterns = [
	url('^login/$', views.Login.as_view()),
	url('^mylogin/$', views.mylogin),

	url('^clientes/findall/$', views.ClientesView.as_view()),
	url('^clientes/form/$', views.ClientesForm.as_view()),
	url('^clientes/form/(?P<pk>\d+)/$', views.ClientesForm.as_view()),

	url('^clientesvscredenciales/findall/$', views.ClientesVsCredencialesView.as_view()),
	url('^clientesvscredenciales/form/$', views.ClientesVsCredencialesForm.as_view()),
	url('^clientesvscredenciales/form/(?P<pk>\d+)/$', views.ClientesVsCredencialesForm.as_view()),

	url('^credenciales/findall/$', views.CredencialesView.as_view()),
	url('^credenciales/form/$', views.CredencialesForm.as_view()),
	url('^credenciales/form/(?P<pk>\d+)/$', views.CredencialesForm.as_view()),

	url('^facturas/findall/$', views.FacturasView.as_view()),
	url('^facturas/form/$', views.FacturasForm.as_view()),
	url('^facturas/form/(?P<pk>\d+)/$', views.FacturasForm.as_view()),

	url('^parqueo/findall/$', views.ParqueoView.as_view()),
	url('^parqueo/form/$', views.ParqueoForm.as_view()),
	url('^parqueo/form/(?P<pk>\d+)/$', views.ParqueoForm.as_view()),

	url('^parqueovsclientes/findall/$', views.ParqueoVsClientesView.as_view()),
	url('^parqueovsclientes/form/$', views.ParqueoVsClientesForm.as_view()),
	url('^parqueovsclientes/form/(?P<pk>\d+)/$', views.ParqueoVsClientesForm.as_view()),

	url('^roles/findall/$', views.RolesView.as_view()),
	url('^roles/form/$', views.RolesForm.as_view()),
	url('^roles/form/(?P<pk>\d+)/$', views.RolesForm.as_view()),

	url('^tarifas/findall/$', views.TarifasView.as_view()),
	url('^tarifas/form/$', views.TarifasForm.as_view()),
	url('^tarifas/form/(?P<pk>\d+)/$', views.TarifasForm.as_view()),

	url('^tpvehiculo/findall/$', views.TpVehiculoView.as_view()),
	url('^tpvehiculo/form/$', views.TpVehiculoForm.as_view()),
	url('^tpvehiculo/form/(?P<pk>\d+)/$', views.TpVehiculoForm.as_view()),

	url('^usuarios/findall/$', views.UsuariosView.as_view()),
	url('^usuarios/form/$', views.UsuariosForm.as_view()),
	url('^usuarios/form/(?P<pk>\d+)/$', views.UsuariosForm.as_view()),

	url('^usuariosvscredenciales/findall/$', views.UsuariosVsCredencialesView.as_view()),
	url('^usuariosvscredenciales/form/$', views.UsuariosVsCredencialesForm.as_view()),
	url('^usuariosvscredenciales/form/(?P<pk>\d+)/$', views.UsuariosVsCredencialesForm.as_view()),

	url('^vehiculos/findall/$', views.VehiculosView.as_view()),
	url('^vehiculos/form/$', views.VehiculosForm.as_view()),
	url('^vehiculos/form/(?P<pk>\d+)/$', views.VehiculosForm.as_view()),

	url('^vehiculosvsclientes/findall/$', views.VehiculosVsClientesView.as_view()),
	url('^vehiculosvsclientes/form/$', views.VehiculosVsClientesForm.as_view()),
	url('^vehiculosvsclientes/form/(?P<pk>\d+)/$', views.VehiculosVsClientesForm.as_view()),

	url('^vehiculosvsparqueo/findall/$', views.VehiculosVsParqueoView.as_view()),
	url('^vehiculosvsparqueo/form/$', views.VehiculosVsParqueoForm.as_view()),
	url('^vehiculosvsparqueo/form/(?P<pk>\d+)/$', views.VehiculosVsParqueoForm.as_view()),

	url('^zonas/findall/$', views.ZonasView.as_view()),
	url('^zonas/form/$', views.ZonasForm.as_view()),
	url('^zonas/form/(?P<pk>\d+)/$', views.ZonasForm.as_view()),

]
