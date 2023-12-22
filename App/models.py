from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock_disponible = models.IntegerField()
    fecha_creacion = models.DateField(auto_now_add=True)
    categoria = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Producto'
