from django.db import models
from django.utils import timezone 
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.

class TipoCombustible(models.Model):
    nombre = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'tipo combustible',
        verbose_name_plural = 'tipo combustible'
    
    def __str__(self):
        return f'{self.nombre}'

class MedidaCombustible(models.Model):
    nombre = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'medida combustible',
        verbose_name_plural = 'medidas combustible'
    
    def __str__(self):
        return f'{self.nombre}'
    
class Ruta(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'ruta',
        verbose_name_plural = 'rutas'
    
    def __str__(self):
        return f'{self.nombre}'

class Marca(models.Model):
    nombre = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'marca',
        verbose_name_plural = 'marcas'
    
    def __str__(self):
        return f'{self.nombre}'

class ClaseVehiculo(models.Model):
    nombre = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'clase vehiculo',
        verbose_name_plural = 'clases vehiculo'
    
    def __str__(self):
        return f'{self.nombre}'

class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'tipo vehiculo',
        verbose_name_plural = 'tipo vehiculo'
    
    def __str__(self):
        return f'{self.nombre}'
    
    
class Vehiculo(models.Model):
    placa = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, null=True, blank=True)
    clase_vehiculo = models.ForeignKey(ClaseVehiculo, on_delete=models.PROTECT, null=True, blank=True)
    tipo_vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.PROTECT, null=True, blank=True)
    tipo_combustible = models.ForeignKey(TipoCombustible, on_delete=models.PROTECT, null=True, blank=True)
    numero_motor = models.CharField(max_length=500)
    numero_chasis = models.CharField(max_length=500)
    year_fabricacion = models.CharField(max_length=100)
    capacidad = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'vehiculo',
        verbose_name_plural = 'vehiculos'
    
    def __str__(self):
        return f'{self.placa}'
    
class Conductor(models.Model):
    nombres = models.CharField(max_length=1000)
    cedula = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=30, null=True, blank=True)
    correo = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'conductor',
        verbose_name_plural = 'conductores'
    
    def __str__(self):
        return f'{self.nombres}'
    
class Orden(models.Model):
    numero_orden = models.IntegerField()
    conductor = models.ForeignKey(Conductor, on_delete=models.PROTECT, null=True, blank=True)
    vehiculo = models.ForeignKey(Vehiculo,  on_delete=models.PROTECT, null=True, blank=True)
    ruta = models.ForeignKey(Ruta,  on_delete=models.PROTECT, null=True, blank=True)
    galones_solicitados = models.IntegerField()
    kilometraje = models.IntegerField()
    fecha_orden = models.DateField(default=timezone.now)
    fecha_ticket = models.DateField(default=timezone.now)
    galones_despachados = models.IntegerField()
    valor = models.DecimalField(max_digits=9, decimal_places=2, default='0', validators=[MinValueValidator(Decimal('0.00'))])
    tipo_medida = models.ForeignKey(MedidaCombustible, on_delete=models.PROTECT, null=True, blank=True)
    observacion = models.TextField(null=True, blank=True)
    # tipo_combustible = models.ForeignKey(TipoCombustible,  on_delete=models.PROTECT, null=True, blank=True)


    class Meta:
        verbose_name = 'orden',
        verbose_name_plural = 'orden'
    
    def __str__(self):
        return f'{self.numero_orden}'