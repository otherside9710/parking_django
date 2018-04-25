# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from supra import views as supra
import models

class ClientesView(supra.SupraListView):
	model = models.Clientes
	search_fields = ['clie_nombres']
	paginate_by=10
# end class

class ClientesVsCredencialesView(supra.SupraListView):
	model = models.ClientesVsCredenciales
# end class

class CredencialesView(supra.SupraListView):
	model = models.Credenciales
# end class

class FacturasView(supra.SupraListView):
	model = models.Facturas
# end class

class ParqueoView(supra.SupraListView):
	model = models.Parqueo
# end class

class ParqueoVsClientesView(supra.SupraListView):
	model = models.ParqueoVsClientes
# end class

class RolesView(supra.SupraListView):
	model = models.Roles
# end class

class TarifasView(supra.SupraListView):
	model = models.Tarifas
# end class

class TpVehiculoView(supra.SupraListView):
	model = models.TpVehiculo
# end class

class UsuariosView(supra.SupraListView):
	model = models.Usuarios
# end class

class UsuariosVsCredencialesView(supra.SupraListView):
	model = models.UsuariosVsCredenciales
# end class

class VehiculosView(supra.SupraListView):
	model = models.Vehiculos
# end class

class VehiculosVsClientesView(supra.SupraListView):
	model = models.VehiculosVsClientes
# end class

class VehiculosVsParqueoView(supra.SupraListView):
	model = models.VehiculosVsParqueo
# end class

class ZonasView(supra.SupraListView):
	model = models.Zonas
# end class

