from django.db import models

class GastoPago(models.Model):
    numero_departamento = models.IntegerField()
    mes = models.CharField(max_length=20)
    anio = models.IntegerField()
    gasto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Depto: {self.numero_departamento} - {self.mes}/{self.anio}"
