from django.urls import path
from . import views  # Importa las vistas de tu archivo views.py

urlpatterns = [
    # Ruta a la página principal
    path('', views.home, name='home'),

    # Ruta para ver todos los gastos (y pagos asociados)
     path('ver_gastos/', views.ver_gastos, name='ver_gastos'),

    # Ruta para generar un nuevo gasto
    path('generar/', views.generar_gasto, name='generar_gasto'),

    # Ruta para registrar un pago
    path('pago/', views.registrar_pago, name='registrar_pago'),
]
