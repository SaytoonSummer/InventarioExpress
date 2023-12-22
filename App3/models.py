from django.db import models
from App2.models import Cliente
from App.models import Producto


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=100)
    metodo_pago = models.CharField(
        max_length=100, default='Tarjeta de crédito')
    direccion_entrega = models.CharField(max_length=255)
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2)
    productos = models.ManyToManyField(Producto, through='DetallePedido')

    def __str__(self):
        return f"Pedido {self.id} - Cliente: {self.cliente.nombre}"

    class Meta:
        db_table = 'pedido'


class DetallePedido(models.Model):
    pedido = models.ForeignKey(
        Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"DetallePedido {self.id} - Pedido {self.pedido.id}, Producto {self.producto.nombre}"

    class Meta:
        db_table = 'detallepedido'
