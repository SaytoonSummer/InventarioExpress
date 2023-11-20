from django.contrib import admin
from .models import Pedido, DetallePedido


class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1


class PedidoAdmin(admin.ModelAdmin):
    inlines = [DetallePedidoInline]


admin.site.register(Pedido, PedidoAdmin)
