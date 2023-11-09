from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio',
                    'stock_disponible', 'fecha_creacion', 'categoria')
    search_fields = ('nombre', 'categoria')
    list_filter = ('categoria',)
    ordering = ('nombre',)

    fieldsets = (
        ('Información del Producto', {
            'fields': ('nombre', 'descripcion', 'precio', 'stock_disponible', 'fecha_creacion', 'categoria')
        }),
    )
