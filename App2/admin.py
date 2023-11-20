from django.contrib import admin
from App2.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['idCliente', 'nombre', 'correo',
                    'direccion', 'telefono', 'fechaRegistro', 'tipoCliente']
    list_editable = ['nombre', 'correo',
                     'direccion', 'telefono', 'tipoCliente']


# Register your models here.
admin.site.register(Cliente, ClienteAdmin)
