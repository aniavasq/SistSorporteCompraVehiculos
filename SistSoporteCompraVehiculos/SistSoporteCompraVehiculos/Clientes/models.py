from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombres = models.CharField(null=True, blank=True, max_length=30)
    apellidos = models.CharField(null=True, blank=True, max_length=30)
    cedula = models.CharField(null=True, blank=True, max_length=10)
    correo = models.EmailField(null=True, blank=True)
    fecha_nacimmiento = models.DateField(null=True, blank=True)
    usuario = models.CharField(null=True, blank=True, max_length=30)
    password = models.CharField(null=True, blank=True, max_length=30)
    is_admin = models.NullBooleanField(null=True, blank=True)
    
class NecesidadCliente(models.Model):
    id_necesidad_cliente = models.AutoField(primary_key=True)
    sueldo = models.FloatField(null=True, blank=True)
    num_integrantes_famil = models.IntegerField(null=True, blank=True)
    promedio_horas_uso_auto = models.FloatField(null=True, blank=True)
    num_integrantes_trabaja = models.IntegerField(null=True, blank=True)
    presupuesto_mensual = models.FloatField(null=True, blank=True)
    id_cliente = models.ForeignKey(Cliente)
    