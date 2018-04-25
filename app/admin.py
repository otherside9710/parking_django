# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models

admin.site.register(models.Clientes)
admin.site.register(models.ClientesVsCredenciales)
admin.site.register(models.Credenciales)
admin.site.register(models.Facturas)
admin.site.register(models.Parqueo)
admin.site.register(models.ParqueoVsClientes)
admin.site.register(models.Roles)
admin.site.register(models.Tarifas)
admin.site.register(models.TpVehiculo)
admin.site.register(models.Usuarios)
admin.site.register(models.UsuariosVsCredenciales)
admin.site.register(models.Vehiculos)
admin.site.register(models.VehiculosVsClientes)
admin.site.register(models.VehiculosVsParqueo)
admin.site.register(models.Zonas)