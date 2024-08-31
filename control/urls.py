from django.urls import path
from . import views

urlpatterns =[
    path('',views.singin, name ='singin'),
    path('exit',views.exit, name ='exit'),
    path('dashboard',views.dashboard, name ='dashboard'),
    path('create-superuser/', views.create_superuser_view, name='create_superuser'),
     # Propiedad
    path('medida_combustible_form/<int:object_pk>/',views.medida_combustible_form, name ='medida_combustible_form'),
    path('medida_combustible_form/',views.medida_combustible_form, name ='medida_combustible_form'),
    path('medida_combustible_list/',views.medida_combustible_list, name ='medida_combustible_list'),
    path('medida_combustible_delete/<int:object_pk>/',views.medida_combustible_delete, name ='medida_combustible_delete'),

    # Tipo Vehículo
    path('tipo_vehiculo_form/<int:object_pk>/',views.tipo_vehiculo_form, name ='tipo_vehiculo_form'),
    path('tipo_vehiculo_form/',views.tipo_vehiculo_form, name ='tipo_vehiculo_form'),
    path('tipo_vehiculo_list/',views.tipo_vehiculo_list, name ='tipo_vehiculo_list'),
    path('tipo_vehiculo_delete/<int:object_pk>/',views.tipo_vehiculo_delete, name ='tipo_vehiculo_delete'),

    # Clases Vehículo
    path('clase_vehiculo_form/<int:object_pk>/',views.clase_vehiculo_form, name ='clase_vehiculo_form'),
    path('clase_vehiculo_form/',views.clase_vehiculo_form, name ='clase_vehiculo_form'),
    path('clase_vehiculo_list/',views.clase_vehiculo_list, name ='clase_vehiculo_list'),
    path('clase_vehiculo_delete/<int:object_pk>/',views.clase_vehiculo_delete, name ='clase_vehiculo_delete'),

     # Marcas Vehículo
    path('marca_form/<int:object_pk>/',views.marca_form, name ='marca_form'),
    path('marca_form/',views.marca_form, name ='marca_form'),
    path('marca_list/',views.marca_list, name ='marca_list'),
    path('marca_delete/<int:object_pk>/',views.marca_delete, name ='marca_delete'),
    path('crear-marca/', views.crear_marca, name='crear_marca'),

    # Tipos combustible
    path('tipo_combustible_form/<int:object_pk>/',views.tipo_combustible_form, name ='tipo_combustible_form'),
    path('tipo_combustible_form/',views.tipo_combustible_form, name ='tipo_combustible_form'),
    path('tipo_combustible_list/',views.tipo_combustible_list, name ='tipo_combustible_list'),
    path('tipo_combustible_delete/<int:object_pk>/',views.tipo_combustible_delete, name ='tipo_combustible_delete'),

    # Ruta
    path('ruta_form/<int:object_pk>/',views.ruta_form, name ='ruta_form'),
    path('ruta_form/',views.ruta_form, name ='ruta_form'),
    path('ruta_list/',views.ruta_list, name ='ruta_list'),
    path('ruta_delete/<int:object_pk>/',views.ruta_delete, name ='ruta_delete'),

    # Vehiculo
    path('vehiculo_form/<int:object_pk>/',views.vehiculo_form, name ='vehiculo_form'),
    path('vehiculo_form/',views.vehiculo_form, name ='vehiculo_form'),
    path('vehiculo_list/',views.vehiculo_list, name ='vehiculo_list'),
    path('vehiculo_delete/<int:object_pk>/',views.vehiculo_delete, name ='vehiculo_delete'),

    # Conductor
    path('conductor_form/<int:object_pk>/',views.conductor_form, name ='conductor_form'),
    path('conductor_form/',views.conductor_form, name ='conductor_form'),
    path('conductor_list/',views.conductor_list, name ='conductor_list'),
    path('conductor_delete/<int:object_pk>/',views.conductor_delete, name ='conductor_delete'),

    # Ordenes
    path('orden_form/<int:object_pk>/',views.orden_form, name ='orden_form'),
    path('orden_form/',views.orden_form, name ='orden_form'),
    path('orden_list/',views.orden_list, name ='orden_list'),
    path('orden_delete/<int:object_pk>/',views.orden_delete, name ='orden_delete'),
    path('orden_conbustible/<int:object_pk>/',views.orden_conbustible, name ='orden_conbustible'),

    #Informes
    path('generar_informe/',views.generar_informe, name ='generar_informe'),
    
]