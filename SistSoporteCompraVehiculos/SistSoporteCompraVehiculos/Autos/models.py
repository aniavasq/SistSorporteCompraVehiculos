from django.db import models


CHOICE_TIPO_COMBUSTIBLE = (
                          ('D','Diesel'),
                          ('G','Gasolina'),
                          ('H','Hibrido'),
                          )
CHOICE_TIPO_AUTO = (
                        ('F','familiar'),
                        ('H','hatchback'),
                        ('L','liftback'),
                        ('S','sedan'),
                        ('D','deportivo'),
                        ('M','monovolumen'),
                        ('T','todoterreno'),
                        ('U','SUV'),
                        ('G','furgoneta'),
                        ('C','camioneta'),
                        )

class Automotor(models.Model):
    id_auto = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=30, null=True, blank=True)
    consumo = models.FloatField(null=True, blank=True)
    precio = models.FloatField(null=True, blank=True)
    capacidad = models.IntegerField(null=True, blank=True)
    costo_mantenimiento = models.FloatField(null=True, blank=True)
    tipo_combustible = models.CharField(null=True, blank=True, choices=CHOICE_TIPO_COMBUSTIBLE, max_length=30)
    tipo_auto = models.CharField(null=True, blank=True, choices=CHOICE_TIPO_AUTO, max_length=30)
    modelo = models.CharField(null=True, blank=True, max_length=30)
    seguridad = models.TextField(null=True, blank=True, max_length=150)
    potencia = models.IntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return self.marca.__str__()+" "+self.modelo.__str__()
    
class Financiamiento(models.Model):
    id_financiamiento = models.AutoField(primary_key=True)
    id_auto = models.ForeignKey(Automotor)
    porcentaje_interes = models.FloatField(null=True, blank=True)
    porcentaje_entrada = models.FloatField(null=True, blank=True)
    anio_financiamiento = models.IntegerField(null=True, blank=True)
    