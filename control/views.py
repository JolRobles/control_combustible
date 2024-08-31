from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.   
def singin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # Si el inicio de sesión es exitoso, redirigir al usuario a alguna página
            return redirect('dashboard')  # Cambia 'dashboard' por el nombre de la URL a la que quieres redirigir
        else:
            # Si las credenciales son incorrectas, mostrar un mensaje de error
            messages.error(request, 'Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.')
            return render(request, 'control/singin.html')
    else:
        # Si la solicitud no es POST, simplemente renderizar la página de inicio de sesión
        return render(request, 'control/singin.html')

@login_required
def exit(request):
    logout(request)
    return redirect('singin')


@login_required
def dashboard(request):

    return render(request, 'control/dashboard.html')

#Medidas Combustible
@login_required
def medida_combustible_form(request, object_pk=None):
    medida_combustible_form = MedidaCombustibleForm()
    title = "Crear Medida de Combustible"
    mensaje = "Registro creado con éxito"
    if object_pk:
        medida_object = MedidaCombustible.objects.get(pk=object_pk)
        medida_combustible_form = MedidaCombustibleForm(instance=medida_object)
        title = "Editar datos de la medida de combustible"
        mensaje = "Registro actualizado con éxito"

    if request.method == 'POST':
        medida_combustible_form = MedidaCombustibleForm(request.POST, request.FILES)
        if object_pk:
            medida_combustible_form = MedidaCombustibleForm(request.POST, request.FILES, instance=medida_object)
        if medida_combustible_form.is_valid():
            medida = medida_combustible_form.save()
            messages.success(request, mensaje)
            return redirect ('medida_combustible_list')

    context = {
        'medida_combustible_form':medida_combustible_form,
        'title':title,
    }

    return render(request, 'configuracion/medida_combustible_form.html', context)

@login_required
def medida_combustible_list(request):
    medidas = MedidaCombustible.objects.all()
    context = {
        'medidas':medidas,
    }
    return render(request, 'configuracion/medida_combustible_list.html', context)


@login_required
def medida_combustible_delete(request, object_pk):
    medida_object = MedidaCombustible.objects.get(pk=object_pk)
    if request.method == 'POST':
        medida_object.delete()
        messages.success(request, "Registro Eliminado con éxito")
        return redirect ('medida_combustible_list')
    context = {
        'medida_object':medida_object,
    }
    return render(request, 'configuracion/medida_combustible_delete.html', context)

#Tipo de Vehiculo
@login_required
def tipo_vehiculo_form(request, object_pk=None):
    tipo_vehiculo_form = TipoVehiculoForm()
    title = "Crear tipo de vehículo"
    mensaje = "Registro creado con éxito"
    if object_pk:
        tipo_vehiculo_object = TipoVehiculo.objects.get(pk=object_pk)
        tipo_vehiculo_form = TipoVehiculoForm(instance=tipo_vehiculo_object)
        title = "Editar datos de la tipo de vehículo"
        mensaje = "Registro actualizado con éxito"

    if request.method == 'POST':
        tipo_vehiculo_form = TipoVehiculoForm(request.POST, request.FILES)
        if object_pk:
            tipo_vehiculo_form = TipoVehiculoForm(request.POST, request.FILES, instance=tipo_vehiculo_object)
        if tipo_vehiculo_form.is_valid():
            tipo_vehiculo = tipo_vehiculo_form.save()
            messages.success(request, mensaje)
            return redirect ('tipo_vehiculo_list')

    context = {
        'tipo_vehiculo_form':tipo_vehiculo_form,
        'title':title,
    }

    return render(request, 'configuracion/tipo_vehiculo_form.html', context)

@login_required
def tipo_vehiculo_list(request):
    tipos_vehiculo = TipoVehiculo.objects.all()
    context = {
        'tipos_vehiculo':tipos_vehiculo,
    }
    return render(request, 'configuracion/tipo_vehiculo_list.html', context)


@login_required
def tipo_vehiculo_delete(request, object_pk):
    tipo_vehiculo_object = TipoVehiculo.objects.get(pk=object_pk)
    if request.method == 'POST':
        tipo_vehiculo_object.delete()
        messages.success(request, "Registro Eliminado con éxito")
        return redirect ('tipo_vehiculo_list')
    context = {
        'tipo_vehiculo_object':tipo_vehiculo_object,
    }
    return render(request, 'configuracion/tipo_vehiculo_delete.html', context)

#Clase de Vehiculo
@login_required
def clase_vehiculo_form(request, object_pk=None):
    clase_vehiculo_form = ClaseVehiculoForm()
    title = "Crear clase de vehículo"
    mensaje = "Registro creado con éxito"
    if object_pk:
        clase_vehiculo_object = ClaseVehiculo.objects.get(pk=object_pk)
        clase_vehiculo_form = ClaseVehiculoForm(instance=clase_vehiculo_object)
        title = "Editar datos de la clase de vehículo"
        mensaje = "Registro actualizado con éxito"

    if request.method == 'POST':
        clase_vehiculo_form = ClaseVehiculoForm(request.POST, request.FILES)
        if object_pk:
            clase_vehiculo_form = ClaseVehiculoForm(request.POST, request.FILES, instance=clase_vehiculo_object)
        if clase_vehiculo_form.is_valid():
            clase_vehiculo = clase_vehiculo_form.save()
            messages.success(request, mensaje)
            return redirect ('clase_vehiculo_list')

    context = {
        'clase_vehiculo_form':clase_vehiculo_form,
        'title':title,
    }

    return render(request, 'configuracion/clase_vehiculo_form.html', context)

@login_required
def clase_vehiculo_list(request):
    clases_vehiculo = ClaseVehiculo.objects.all()
    context = {
        'clases_vehiculo':clases_vehiculo,
    }
    return render(request, 'configuracion/clase_vehiculo_list.html', context)


@login_required
def clase_vehiculo_delete(request, object_pk):
    clase_vehiculo_object = ClaseVehiculo.objects.get(pk=object_pk)
    if request.method == 'POST':
        clase_vehiculo_object.delete()
        messages.success(request, "Registro Eliminado con éxito")
        return redirect ('clase_vehiculo_list')
    context = {
        'clase_vehiculo_object':clase_vehiculo_object,
    }
    return render(request, 'configuracion/clase_vehiculo_delete.html', context)


#Marca de Vehiculo
@login_required
def marca_form(request, object_pk=None):
    marca_form = MarcaForm()
    title = "Crear marca de vehículo"
    mensaje = "Registro creado con éxito"
    if object_pk:
        marca_object = Marca.objects.get(pk=object_pk)
        marca_form = MarcaForm(instance=marca_object)
        title = "Editar datos de la marca de vehículo"
        mensaje = "Registro actualizado con éxito"

    if request.method == 'POST':
        marca_form = MarcaForm(request.POST, request.FILES)
        if object_pk:
            marca_form = MarcaForm(request.POST, request.FILES, instance=marca_object)
        if marca_form.is_valid():
            marca = marca_form.save()
            messages.success(request, mensaje)
            return redirect ('marca_list')

    context = {
        'marca_form':marca_form,
        'title':title,
    }

    return render(request, 'configuracion/marca_form.html', context)


def crear_marca(request):
    print("llega a crear marca")
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            nueva_marca = form.save()
            return JsonResponse({'id': nueva_marca.id, 'nombre': nueva_marca.nombre}, status=201)
        return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = MarcaForm()
    return render(request, 'crear_marca.html', {'form': form})

@login_required
def marca_list(request):
    marcas = Marca.objects.all()
    context = {
        'marcas':marcas,
    }
    return render(request, 'configuracion/marca_list.html', context)


@login_required
def marca_delete(request, object_pk):
    marca_object = Marca.objects.get(pk=object_pk)
    if request.method == 'POST':
        marca_object.delete()
        messages.success(request, "Registro Eliminado con éxito")
        return redirect ('marca_list')
    context = {
        'marca_object':marca_object,
    }
    return render(request, 'configuracion/marca_delete.html', context)

#Tipo de combustible
@login_required
def tipo_combustible_form(request, object_pk=None):
    tipo_combustible_form = TipoCombustibleForm()
    title = "Crear tipo de combustible"
    mensaje = "Registro creado con éxito"
    if object_pk:
        tipo_combustible_object = TipoCombustible.objects.get(pk=object_pk)
        tipo_combustible_form = TipoCombustibleForm(instance=tipo_combustible_object)
        title = "Editar datos de tipo combustible"
        mensaje = "Registro actualizado con éxito"

    if request.method == 'POST':
        tipo_combustible_form = TipoCombustibleForm(request.POST, request.FILES)
        if object_pk:
            tipo_combustible_form = TipoCombustibleForm(request.POST, request.FILES, instance=tipo_combustible_object)
        if tipo_combustible_form.is_valid():
            tipo_combustible = tipo_combustible_form.save()
            messages.success(request, mensaje)
            return redirect ('tipo_combustible_list')

    context = {
        'tipo_combustible_form':tipo_combustible_form,
        'title':title,
    }

    return render(request, 'configuracion/tipo_combustible_form.html', context)

@login_required
def tipo_combustible_list(request):
    tipos_combustible = TipoCombustible.objects.all()
    context = {
        'tipos_combustible':tipos_combustible,
    }
    return render(request, 'configuracion/tipo_combustible_list.html', context)


@login_required
def tipo_combustible_delete(request, object_pk):
    tipo_combustible_object = TipoCombustible.objects.get(pk=object_pk)
    if request.method == 'POST':
        tipo_combustible_object.delete()
        messages.success(request, "Registro Eliminado con éxito")
        return redirect ('tipo_combustible_list')
    context = {
        'tipo_combustible_object':tipo_combustible_object,
    }
    return render(request, 'configuracion/tipo_combustible_delete.html', context)

#Rutas
@login_required
def ruta_form(request, object_pk=None):
    ruta_form = RutaForm()
    title = "Crear ruta"
    mensaje = "Registro creado con éxito"
    if object_pk:
        ruta_object = Ruta.objects.get(pk=object_pk)
        ruta_form = RutaForm(instance=ruta_object)
        title = "Editar datos de ruta"
        mensaje = "Registro actualizado con éxito"

    if request.method == 'POST':
        ruta_form = RutaForm(request.POST, request.FILES)
        if object_pk:
            ruta_form = RutaForm(request.POST, request.FILES, instance=ruta_object)
        if ruta_form.is_valid():
            ruta = ruta_form.save()
            messages.success(request, mensaje)
            return redirect ('ruta_list')

    context = {
        'ruta_form':ruta_form,
        'title':title,
    }

    return render(request, 'configuracion/ruta_form.html', context)

@login_required
def ruta_list(request):
    rutas = Ruta.objects.all()
    context = {
        'rutas':rutas,
    }
    return render(request, 'configuracion/ruta_list.html', context)


@login_required
def ruta_delete(request, object_pk):
    ruta_object = Ruta.objects.get(pk=object_pk)
    if request.method == 'POST':
        ruta_object.delete()
        messages.success(request, "Registro Eliminado con éxito")
        return redirect ('ruta_list')
    context = {
        'ruta_object':ruta_object,
    }
    return render(request, 'configuracion/ruta_delete.html', context)

#Vehiculos
@login_required
def vehiculo_form(request, object_pk=None):
    vehiculo_form = VehiculoForm()
    marca_form = MarcaForm()
    title = "Crear vehículo"
    mensaje = "Registro creado con éxito"
    if object_pk:
        vehiculo_object = Vehiculo.objects.get(pk=object_pk)
        vehiculo_form = VehiculoForm(instance=vehiculo_object)
        title = "Editar datos de vehículo"
        mensaje = "Registro actualizado con éxito"

    if request.method == 'POST':
        vehiculo_form = VehiculoForm(request.POST, request.FILES)
        if object_pk:
            vehiculo_form = VehiculoForm(request.POST, request.FILES, instance=vehiculo_object)
        if vehiculo_form.is_valid():
            vehiculo = vehiculo_form.save()
            messages.success(request, mensaje)
            return redirect ('vehiculo_list')

    context = {
        'vehiculo_form':vehiculo_form,
        'marca_form':marca_form,
        'title':title,
    }

    return render(request, 'configuracion/vehiculo_form.html', context)

@login_required
def vehiculo_list(request):
    vehiculos = Vehiculo.objects.all()
    context = {
        'vehiculos':vehiculos,
    }
    return render(request, 'configuracion/vehiculo_list.html', context)


@login_required
def vehiculo_delete(request, object_pk):
    vehiculo_object = Vehiculo.objects.get(pk=object_pk)
    if request.method == 'POST':
        vehiculo_object.delete()
        messages.success(request, "Registro Eliminado con éxito")
        return redirect ('vehiculo_list')
    context = {
        'vehiculo_object':vehiculo_object,
    }
    return render(request, 'configuracion/vehiculo_delete.html', context)

#Conductores
@login_required
def conductor_form(request, object_pk=None):
    conductor_form = ConductorForm()
    title = "Crear conductor"
    mensaje = "Registro creado con éxito"
    if object_pk:
        conductor_object = Conductor.objects.get(pk=object_pk)
        conductor_form = ConductorForm(instance=conductor_object)
        title = "Editar datos de conductor"
        mensaje = "Registro actualizado con éxito"

    if request.method == 'POST':
        conductor_form = ConductorForm(request.POST, request.FILES)
        if object_pk:
            conductor_form = ConductorForm(request.POST, request.FILES, instance=conductor_object)
        if conductor_form.is_valid():
            conductor = conductor_form.save()
            messages.success(request, mensaje)
            return redirect ('conductor_list')

    context = {
        'conductor_form':conductor_form,
        'title':title,
    }

    return render(request, 'configuracion/conductor_form.html', context)

@login_required
def conductor_list(request):
    conductores = Conductor.objects.all()
    context = {
        'conductores':conductores,
    }
    return render(request, 'configuracion/conductor_list.html', context)


@login_required
def conductor_delete(request, object_pk):
    conductor_object = Conductor.objects.get(pk=object_pk)
    if request.method == 'POST':
        conductor_object.delete()
        messages.success(request, "Registro Eliminado con éxito")
        return redirect ('conductor_list')
    context = {
        'conductor_object':conductor_object,
    }
    return render(request, 'configuracion/conductor_delete.html', context)

#Ordenes
@login_required
def orden_form(request, object_pk=None):
    orden_form = OrdenForm()
    title = "Crear orden de combustible"
    mensaje = "Registro creado con éxito"
    if object_pk:
        orden_object = Orden.objects.get(pk=object_pk)
        orden_form = OrdenForm(instance=orden_object)
        title = "Editar datos de orden de combustible"
        mensaje = "Registro actualizado con éxito"

    if request.method == 'POST':
        orden_form = OrdenForm(request.POST, request.FILES)
        if object_pk:
            orden_form = OrdenForm(request.POST, request.FILES, instance=orden_object)
        if orden_form.is_valid():
            orden = orden_form.save()
            messages.success(request, mensaje)
            return redirect ('orden_list')

    context = {
        'orden_form':orden_form,
        'title':title,
    }

    return render(request, 'configuracion/orden_form.html', context)

@login_required
def orden_list(request):
    ordenes = Orden.objects.all()
    context = {
        'ordenes':ordenes,
    }
    return render(request, 'configuracion/orden_list.html', context)


@login_required
def orden_delete(request, object_pk):
    orden_object = Orden.objects.get(pk=object_pk)
    if request.method == 'POST':
        orden_object.delete()
        messages.success(request, "Registro Eliminado con éxito")
        return redirect ('orden_list')
    context = {
        'orden_object':orden_object,
    }
    return render(request, 'configuracion/orden_delete.html', context)

@login_required
def orden_conbustible(request, object_pk):
    orden_object = Orden.objects.get(pk=object_pk)
    tipos_combustible = TipoCombustible.objects.all()
    fecha_actual = timezone.now()
    numero_orden = str(orden_object.numero_orden).zfill(7) 
    context = {
        'orden_object':orden_object,
        'tipos_combustible':tipos_combustible,
        'fecha_actual':fecha_actual,
        'numero_orden':numero_orden,
    }

    return render(request, 'configuracion/orden_combustible.html', context)

@login_required
def generar_informe(request):
     informe_form = GenerarInformeForm()
     if request.method == "POST":
        vehiculo = request.POST.get('vehiculo')
        conductor = request.POST.get('conductor')
        combustible = request.POST.get('combustible')
        ruta = request.POST.get('ruta')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        ordenes = Orden.objects.filter(fecha_orden__range = [fecha_inicio, fecha_fin])
        if vehiculo:
            ordenes = ordenes.filter(vehiculo__pk=vehiculo)
        if conductor:
            ordenes = ordenes.filter(conductor__pk=conductor)
        if combustible:
            ordenes = ordenes.filter(combustible__pk=combustible)
        if ruta:
            ordenes = ordenes.filter(ruta__pk=ruta)

        
        context = {
            'title': 'Generar Informe.',
            'informe_form':informe_form,
            'ordenes':ordenes,
        }

        return render(request, 'configuracion/informe.html', context)

     context = {
         'title': 'Generar Informe.',
         'informe_form':informe_form
         
     }
     return render(request, 'configuracion/generar_informe.html', context)