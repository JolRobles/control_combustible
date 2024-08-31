from django import forms

from .models import *
from datetime import datetime

class MedidaCombustibleForm(forms.ModelForm):
    class Meta:
        model = MedidaCombustible
        fields = '__all__'  

class TipoVehiculoForm(forms.ModelForm):
    class Meta:
        model = TipoVehiculo
        fields = '__all__'  

class ClaseVehiculoForm(forms.ModelForm):
    class Meta:
        model = ClaseVehiculo
        fields = '__all__'  

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'  

class TipoCombustibleForm(forms.ModelForm):
    class Meta:
        model = TipoCombustible
        fields = '__all__' 

class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = '__all__' 

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__' 
        labels = {
            'numero_motor':'Numero de Motor',
            'numero_chasis':'Numero de Chasis',
            'year_fabricacion':'Año de fabricación',
        }

class ConductorForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = '__all__' 
        labels = {
            'nombres':'Nombres y Apellidos',
            'cedula':'Cédula',
        }

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'
        widgets = {
            'observacion': forms.Textarea(attrs={'value': 'Observación', 'rows': '1' ,'placeholder':''}) , 
        }
        # labels = {
        #     'nombres':'Nombres y Apellidos',
        #     'cedula':'Cédula',
        # }
    def __init__(self, *args, **kwargs):
        super(OrdenForm, self).__init__(*args, **kwargs)
        last_order = Orden.objects.filter().last()
        numero_orden = 1
        if last_order:
            numero_orden = 1 + int(last_order.numero_orden)
        self.fields['numero_orden'].initial = numero_orden


class GenerarInformeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(GenerarInformeForm, self).__init__(*args, **kwargs)
        vehiculos = [('', '-------------')] + [(obj.pk, obj.placa) for obj in Vehiculo.objects.all()]
        conductores = [('', '-------------')] + [(obj.pk, obj.nombres) for obj in Conductor.objects.all()]
        combustibles = [('', '-------------')] + [(obj.pk, obj.nombre) for obj in TipoCombustible.objects.all()]
        rutas = [('', '-------------')] + [(obj.pk, obj.nombre) for obj in Ruta.objects.all()]
        self.fields['vehiculo'].choices = vehiculos
        self.fields['conductor'].choices = conductores
        self.fields['combustible'].choices = combustibles
        self.fields['ruta'].choices = rutas

    vehiculo = forms.ChoiceField(label='Vehículo', required=False)
    conductor = forms.ChoiceField(label='Conductor', required=False)
    combustible = forms.ChoiceField(label='Combustible', required=False)
    ruta = forms.ChoiceField(label='Ruta', required=False)
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'value': datetime.now().strftime('%Y-%m-%d')}),
        label='Fecha Inicio', required=False
    )
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'value': datetime.now().strftime('%Y-%m-%d')}),
        label='Fecha Fin', required=False
    )