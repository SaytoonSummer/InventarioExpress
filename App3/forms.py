from django import forms
from .models import Pedido, DetallePedido, Producto
from datetime import date
from django.forms import modelformset_factory


class ProductoCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    template_name = 'custom_checkbox_select.html'


class PedidoForm(forms.ModelForm):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Enviado', 'Enviado'),
        ('Entregado', 'Entregado'),
    ]

    METODO_PAGO_CHOICES = [
        ('Tarjeta', 'Tarjeta'),
        ('Transferencia', 'Transferencia'),
        ('Efectivo', 'Efectivo'),
    ]

    estado = forms.ChoiceField(choices=ESTADO_CHOICES)
    metodo_pago = forms.ChoiceField(choices=METODO_PAGO_CHOICES)

    productos = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.all(),
        widget=ProductoCheckboxSelectMultiple,  # Usa el widget personalizado aquí
    )

    class Meta:
        model = Pedido
        fields = ['cliente', 'productos', 'estado',
                  'metodo_pago', 'direccion_entrega']

    def clean_fecha(self):
        return date.today()


class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['producto', 'cantidad']

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        producto = self.cleaned_data.get('producto')

        if cantidad > producto.stock_disponible:
            raise forms.ValidationError(
                "La cantidad solicitada es mayor que el stock disponible.")

        return cantidad


DetallePedidoFormSet = modelformset_factory(
    DetallePedido, form=DetallePedidoForm, extra=1, can_delete=True)
