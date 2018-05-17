# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from supra import views as supra
import models
from django import forms

supra.SupraConf.body = False
supra.SupraConf.template = False
supra.SupraConf.ACCECC_CONTROL["allow"] = True

class Login(supra.SupraSession):
	pass
# end class

def mylogin(request):
	# request.GET.get('key', default)
	# request.POST.get('key', default)
	# request.body
	
	return HttpResponse("Aqui va tu login")
# end def

class ClientesForm(supra.SupraFormView):
	model = models.Clientes
# end class

class ClientesView(supra.SupraListView):
	model = models.Clientes
	search_fields = ['clie_nombres']
	paginate_by=10
# end class

class ClientesVsCredencialesForm(supra.SupraFormView):
	model = models.ClientesVsCredenciales
# end class

class ClientesVsCredencialesView(supra.SupraListView):
	model = models.ClientesVsCredenciales
# end class

class CredencialesForm(supra.SupraFormView):
	model = models.Credenciales
# end class

class CredencialesView(supra.SupraListView):
	model = models.Credenciales
# end class

class FacturasForm(supra.SupraFormView):
	model = models.Facturas
# end class

class FacturasView(supra.SupraListView):
	model = models.Facturas
# end class

class ParqueoForm(supra.SupraFormView):
	model = models.Parqueo
# end class

class ParqueoView(supra.SupraListView):
	model = models.Parqueo
# end class

class ParqueoVsClientesForm(supra.SupraFormView):
	model = models.ParqueoVsClientes
# end class

class ParqueoVsClientesView(supra.SupraListView):
	model = models.ParqueoVsClientes
# end class

class RolesForm(supra.SupraFormView):
	model = models.Roles
# end class

class RolesView(supra.SupraListView):
	model = models.Roles
# end class

class TarifasForm(supra.SupraFormView):
	model = models.Tarifas
# end class

class TarifasView(supra.SupraListView):
	model = models.Tarifas
# end class

class TpVehiculoForm(supra.SupraFormView):
	model = models.TpVehiculo
# end class

class TpVehiculoView(supra.SupraListView):
	model = models.TpVehiculo
# end class

class UsuariosForm(supra.SupraFormView):
	model = models.Usuarios
# end class

class UsuariosView(supra.SupraListView):
	model = models.Usuarios
# end class

class UsuariosVsCredencialesForm(supra.SupraFormView):
	model = models.UsuariosVsCredenciales
# end class

class UsuariosVsCredencialesView(supra.SupraListView):
	model = models.UsuariosVsCredenciales
# end class

class VehiculosForm(supra.SupraFormView):
	model = models.Vehiculos
# end class

class VehiculosView(supra.SupraListView):
	model = models.Vehiculos
# end class

class VehiculosVsClientesForm(supra.SupraFormView):
	model = models.VehiculosVsClientes
# end class

class VehiculosVsClientesView(supra.SupraListView):
	model = models.VehiculosVsClientes
# end class

class VehiculosVsParqueoForm(supra.SupraFormView):
	model = models.VehiculosVsParqueo
# end class

class VehiculosVsParqueoView(supra.SupraListView):
	model = models.VehiculosVsParqueo
# end class

class ZonasForm(supra.SupraFormView):
	model = models.Zonas
# end class

class ZonasView(supra.SupraListView):
	model = models.Zonas
# end class

