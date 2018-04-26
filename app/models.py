# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Clientes(models.Model):
    clie_codigo = models.AutoField(primary_key=True)
    clie_nombres = models.CharField(max_length=100, blank=True, null=True)
    clie_cedula = models.CharField(max_length=50, blank=True, null=True)
    clie_telefono = models.CharField(max_length=50, blank=True, null=True)
    clie_direccion = models.CharField(max_length=50, blank=True, null=True)
    clie_email = models.CharField(max_length=50, blank=True, null=True)
    clie_estado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class ClientesVsCredenciales(models.Model):
    clientes_clie_codigo = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='clientes_clie_codigo', primary_key=True)
    credenciales_cred_codigo = models.ForeignKey('Credenciales', models.DO_NOTHING, db_column='credenciales_cred_codigo')

    class Meta:
        managed = False
        db_table = 'clientes_vs_credenciales'
        unique_together = (('clientes_clie_codigo', 'credenciales_cred_codigo'),)


class Credenciales(models.Model):
    cred_codigo = models.AutoField(primary_key=True)
    cred_cliente = models.IntegerField(blank=True, null=True)
    cred_usuario = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credenciales'


class Facturas(models.Model):
    fact_codigo = models.AutoField(primary_key=True)
    clie_codigo = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='clie_codigo')
    usua_codigo = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='usua_codigo')

    class Meta:
        managed = False
        db_table = 'facturas'
        unique_together = (('fact_codigo', 'clie_codigo', 'usua_codigo'),)


class Parqueo(models.Model):
    par_codigo = models.AutoField(primary_key=True)
    par_vehiculo = models.CharField(max_length=50, blank=True, null=True)
    par_finicio = models.CharField(max_length=50, blank=True, null=True)
    par_ffinal = models.CharField(max_length=50, blank=True, null=True)
    par_estado = models.CharField(max_length=1, blank=True, null=True)
    tari_codigo = models.ForeignKey('Tarifas', models.DO_NOTHING, db_column='tari_codigo')

    class Meta:
        managed = False
        db_table = 'parqueo'
        unique_together = (('par_codigo', 'tari_codigo'),)


class ParqueoVsClientes(models.Model):
    parqueo_par_codigo = models.ForeignKey(Parqueo, models.DO_NOTHING, db_column='parqueo_par_codigo', primary_key=True)
    clientes_clie_codigo = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='clientes_clie_codigo')

    class Meta:
        managed = False
        db_table = 'parqueo_vs_clientes'
        unique_together = (('parqueo_par_codigo', 'clientes_clie_codigo'),)


class Roles(models.Model):
    rol_codigo = models.AutoField(primary_key=True)
    rol_nombre = models.CharField(max_length=50, blank=True, null=True)
    rol_estado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Tarifas(models.Model):
    tari_codigo = models.AutoField(primary_key=True)
    tari_vlrhora = models.FloatField(db_column='tari_vlrHora', blank=True, null=True)  # Field name made lowercase.
    tari_vlrdia = models.FloatField(db_column='tari_vlrDia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tarifas'


class TpVehiculo(models.Model):
    tpv_codigo = models.AutoField(primary_key=True)
    tp_vehiculo = models.IntegerField()
    tp_modelo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tp_vehiculo'


class Usuarios(models.Model):
    usua_codigo = models.AutoField(primary_key=True)
    usua_nombres = models.CharField(max_length=100, blank=True, null=True)
    usua_cedula = models.CharField(max_length=50, blank=True, null=True)
    usua_clave = models.CharField(max_length=45, blank=True, null=True)
    usua_telefono = models.CharField(max_length=50, blank=True, null=True)
    usua_estado = models.CharField(max_length=1, blank=True, null=True)
    rol_codigo = models.ForeignKey(Roles, models.DO_NOTHING, db_column='rol_codigo')

    class Meta:
        managed = False
        db_table = 'usuarios'
        unique_together = (('usua_codigo', 'rol_codigo'),)


class UsuariosVsCredenciales(models.Model):
    usuarios_usua_codigo = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='usuarios_usua_codigo', primary_key=True)
    credenciales_cred_codigo = models.ForeignKey(Credenciales, models.DO_NOTHING, db_column='credenciales_cred_codigo')

    class Meta:
        managed = False
        db_table = 'usuarios_vs_credenciales'
        unique_together = (('usuarios_usua_codigo', 'credenciales_cred_codigo'),)


class Vehiculos(models.Model):
    veh_codigo = models.AutoField(primary_key=True)
    veh_cliente = models.IntegerField(blank=True, null=True)
    veh_placa = models.CharField(max_length=50, blank=True, null=True)
    veh_estado = models.CharField(max_length=1, blank=True, null=True)
    tpv_codigo = models.ForeignKey(TpVehiculo, models.DO_NOTHING, db_column='tpv_codigo')

    class Meta:
        managed = False
        db_table = 'vehiculos'
        unique_together = (('veh_codigo', 'tpv_codigo'),)


class VehiculosVsClientes(models.Model):
    vehiculos_veh_codigo = models.ForeignKey(Vehiculos, models.DO_NOTHING, db_column='vehiculos_veh_codigo', primary_key=True)
    clientes_clie_codigo = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='clientes_clie_codigo')

    class Meta:
        managed = False
        db_table = 'vehiculos_vs_clientes'
        unique_together = (('vehiculos_veh_codigo', 'clientes_clie_codigo'),)


class VehiculosVsParqueo(models.Model):
    vehiculos_veh_codigo = models.ForeignKey(Vehiculos, models.DO_NOTHING, db_column='vehiculos_veh_codigo', primary_key=True)
    parqueo_par_codigo = models.ForeignKey(Parqueo, models.DO_NOTHING, db_column='parqueo_par_codigo')

    class Meta:
        managed = False
        db_table = 'vehiculos_vs_parqueo'
        unique_together = (('vehiculos_veh_codigo', 'parqueo_par_codigo'),)


class Zonas(models.Model):
    zona_codigo = models.AutoField(primary_key=True)
    zona_nombre = models.CharField(max_length=100, blank=True, null=True)
    par_codigo = models.ForeignKey(Parqueo, models.DO_NOTHING, db_column='par_codigo')

    class Meta:
        managed = False
        db_table = 'zonas'
        unique_together = (('zona_codigo', 'par_codigo'),)
