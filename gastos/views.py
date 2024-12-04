from django.shortcuts import render
from django.http import JsonResponse
from firebase_admin import db

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
def generar_gasto(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        monto = request.POST.get('monto')
        numero_departamento = request.POST.get('numero_departamento')
        mes = request.POST.get('mes')
        anio = request.POST.get('anio')

        ref = db.reference('gastos')
        # Crear un gasto en Firebase
        nuevo_gasto = ref.push({
            'descripcion': descripcion,
            'monto': monto,
            'numero_departamento': numero_departamento,
            'mes': mes,
            'anio': anio,
            'pagado': False,  # Marca como no pagado inicialmente
        })
        
        # Obtenemos el ID del gasto creado para asociarlo a los pagos
        gasto_id = nuevo_gasto.key
        return JsonResponse({'status': 'success', 'message': 'Gasto creado correctamente', 'gasto_id': gasto_id})

    return render(request, 'gastos/generar_gasto.html')

# Vista para registrar un pago
def registrar_pago(request):
    if request.method == 'POST':
        numero_departamento = request.POST.get('numero_departamento')
        mes = request.POST.get('mes')
        anio = request.POST.get('anio')

        # Buscar el gasto relacionado con el departamento, mes y año
        ref = db.reference('gastos')
        gastos = ref.order_by_child('numero_departamento').equal_to(numero_departamento).get()

        # Buscar si ya existe un gasto pendiente para el departamento, mes y año
        for gasto_id, gasto_data in gastos.items():
            if gasto_data['mes'] == mes and gasto_data['anio'] == anio and not gasto_data['pagado']:
                # Si encontramos un gasto que no ha sido pagado, lo actualizamos con el pago
                ref.child(gasto_id).update({'pagado': True})

                # Guardar el pago en la base de datos bajo el mismo gasto
                ref_pago = db.reference(f'gastos/{gasto_id}/pagos')  # Subreferencia de pagos dentro del gasto
                ref_pago.push({
                    'numero_departamento': numero_departamento,
                    'mes': mes,
                    'anio': anio,
                    'monto': gasto_data['monto'],
                    'fecha_pago': 'Fecha actual aquí',  # Aquí puedes agregar la fecha actual si lo deseas
                })

                return JsonResponse({'status': 'success', 'message': 'Pago registrado correctamente'})
        
        # Si no se encuentra un gasto pendiente
        return JsonResponse({'status': 'error', 'message': 'No se encontró un gasto pendiente para el departamento y mes especificado'})

    return render(request, 'gastos/registrar_pago.html')
