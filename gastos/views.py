from django.shortcuts import render
from django.http import JsonResponse
from firebase_admin import db
from datetime import datetime

# Vista para la página principal
def home(request):
    return render(request, 'gastos/home.html')

# Vista para ver los gastos
def ver_gastos(request):
    ref = db.reference('gastos')
    gastos = ref.get()  # Obtiene todos los gastos de Firebase

    # Convertir los datos de Firebase en una lista legible
    gastos_list = []
    if gastos:
        for gasto_id, gasto_data in gastos.items():
            gasto_data['id'] = gasto_id  # Añadir el ID único de cada gasto
            gastos_list.append(gasto_data)

    # Pasar los gastos a la plantilla
    return render(request, 'gastos/ver_gastos.html', {'gastos': gastos_list})
# Vista para generar un nuevo gasto
def generar_gasto(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        monto = request.POST.get('monto')
        numero_departamento = request.POST.get('numero_departamento')
        mes = request.POST.get('mes')
        anio = request.POST.get('anio')

        # Validación simple para asegurar que no falten campos
        if not all([descripcion, monto, numero_departamento, mes, anio]):
            return JsonResponse({'status': 'error', 'message': 'Todos los campos son requeridos'})

        try:
            ref = db.reference('gastos')
            # Crear un gasto en Firebase
            nuevo_gasto = ref.push({
                'descripcion': descripcion,
                'monto': float(monto),  # Asegurarse de convertir el monto a tipo float
                'numero_departamento': numero_departamento,
                'mes': mes,
                'anio': anio,
                'pagado': False,  # Marca como no pagado inicialmente
                'fecha_creacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Fecha actual
            })
            
            gasto_id = nuevo_gasto.key  # Obtenemos el ID del gasto creado
            return JsonResponse({'status': 'success', 'message': 'Gasto creado correctamente', 'gasto_id': gasto_id})
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error al crear el gasto: {str(e)}'})

    return render(request, 'gastos/generar_gasto.html')

# Vista para registrar un pago
def registrar_pago(request):
    if request.method == 'POST':
        numero_departamento = request.POST.get('numero_departamento')
        mes = request.POST.get('mes')
        anio = request.POST.get('anio')

        # Validación simple para asegurar que no falten campos
        if not all([numero_departamento, mes, anio]):
            return JsonResponse({'status': 'error', 'message': 'Todos los campos son requeridos'})

        try:
            ref = db.reference('gastos')
            gastos = ref.order_by_child('numero_departamento').equal_to(numero_departamento).get()

            # Buscar si ya existe un gasto pendiente para el departamento, mes y año
            for gasto_id, gasto_data in gastos.items():
                if gasto_data['mes'] == mes and gasto_data['anio'] == anio and not gasto_data['pagado']:
                    # Actualizamos el gasto como pagado
                    ref.child(gasto_id).update({'pagado': True})

                    # Guardar el pago en la base de datos bajo el mismo gasto
                    ref_pago = db.reference(f'gastos/{gasto_id}/pagos')  # Subreferencia de pagos dentro del gasto
                    ref_pago.push({
                        'numero_departamento': numero_departamento,
                        'mes': mes,
                        'anio': anio,
                        'monto': gasto_data['monto'],
                        'fecha_pago': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # Fecha actual
                    })

                    return JsonResponse({'status': 'success', 'message': 'Pago registrado correctamente'})
            
            # Si no se encuentra un gasto pendiente
            return JsonResponse({'status': 'error', 'message': 'No se encontró un gasto pendiente para el departamento y mes especificado'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error al registrar el pago: {str(e)}'})

    return render(request, 'gastos/registrar_pago.html')
