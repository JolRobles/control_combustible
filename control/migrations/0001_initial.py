# Generated by Django 4.2.14 on 2024-07-16 04:22

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClaseVehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': ('clase vehiculo',),
                'verbose_name_plural': 'clases vehiculo',
            },
        ),
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=1000)),
                ('cedula', models.CharField(blank=True, max_length=20, null=True)),
                ('celular', models.CharField(blank=True, max_length=30, null=True)),
                ('correo', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': ('conductor',),
                'verbose_name_plural': 'conductores',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': ('marca',),
                'verbose_name_plural': 'marcas',
            },
        ),
        migrations.CreateModel(
            name='MedidaCombustible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': ('medida combustible',),
                'verbose_name_plural': 'medidas combustible',
            },
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': ('ruta',),
                'verbose_name_plural': 'rutas',
            },
        ),
        migrations.CreateModel(
            name='TipoCombustible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': ('tipo combustible',),
                'verbose_name_plural': 'tipo combustible',
            },
        ),
        migrations.CreateModel(
            name='TipoVehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': ('tipo vehiculo',),
                'verbose_name_plural': 'tipo vehiculo',
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=100)),
                ('numero_motor', models.CharField(max_length=500)),
                ('numero_chasis', models.CharField(max_length=500)),
                ('year_fabricacion', models.CharField(max_length=100)),
                ('capacidad', models.CharField(max_length=100)),
                ('clase_vehiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='control.clasevehiculo')),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='control.marca')),
                ('tipo_vehiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='control.tipovehiculo')),
            ],
            options={
                'verbose_name': ('vehiculo',),
                'verbose_name_plural': 'vehiculos',
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_orden', models.IntegerField()),
                ('galones_solicitados', models.IntegerField()),
                ('kilometraje', models.IntegerField()),
                ('fecha_orden', models.DateField(default=django.utils.timezone.now)),
                ('fecha_ticket', models.DateField(default=django.utils.timezone.now)),
                ('galones_despachados', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, default='0', max_digits=9, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('observacion', models.TextField(blank=True, null=True)),
                ('conductor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='control.conductor')),
                ('ruta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='control.ruta')),
                ('tipo_medida', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='control.medidacombustible')),
                ('vehiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='control.vehiculo')),
            ],
            options={
                'verbose_name': ('orden',),
                'verbose_name_plural': 'orden',
            },
        ),
    ]
