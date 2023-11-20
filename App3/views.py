from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Pedido, DetallePedido
from django.utils import timezone
from .forms import PedidoForm, DetallePedidoForm
from django.db.models import Sum
from django.forms import modelformset_factory
from django.forms import formset_factory


def createpedido(request):
    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        detalle_form = DetallePedidoForm(request.POST)

        if pedido_form.is_valid() and detalle_form.is_valid():
            pedido = pedido_form.save(commit=False)
            pedido.fecha = timezone.now()

            detalle_pedido = detalle_form.save(commit=False)

            if detalle_pedido.cantidad > detalle_pedido.producto.stock_disponible:
                return render(request, 'App3/createpedido.html', {'pedido_form': pedido_form, 'detalle_form': detalle_form, 'error_message': 'Stock insuficiente'})

            pedido.total_pedido = detalle_pedido.cantidad * detalle_pedido.producto.precio
            pedido.save()

            detalle_pedido.producto.stock_disponible -= detalle_pedido.cantidad
            detalle_pedido.producto.save()

            detalle_pedido.pedido = pedido
            detalle_pedido.save()

            return redirect('indexpedido')
    else:
        pedido_form = PedidoForm()
        detalle_form = DetallePedidoForm()

    return render(request, 'App3/createpedido.html', {'pedido_form': pedido_form, 'detalle_form': detalle_form})


def updatepedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    detalle_pedido = get_object_or_404(DetallePedido, pedido=pedido)

    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST, instance=pedido)
        detalle_form = DetallePedidoForm(request.POST, instance=detalle_pedido)

        if pedido_form.is_valid() and detalle_form.is_valid():
            detalle_pedido.producto.stock_disponible += detalle_pedido.cantidad
            detalle_pedido.producto.save()

            pedido = pedido_form.save(commit=False)
            pedido.total_pedido = detalle_form.cleaned_data['cantidad'] * \
                detalle_form.cleaned_data['producto'].precio
            pedido.save()

            detalle_pedido = detalle_form.save(commit=False)
            detalle_pedido.pedido = pedido
            detalle_pedido.save()

            detalle_pedido.producto.stock_disponible -= detalle_pedido.cantidad
            detalle_pedido.producto.save()

            return redirect('indexpedido')
    else:
        pedido_form = PedidoForm(instance=pedido)
        detalle_form = DetallePedidoForm(instance=detalle_pedido)

    context = {'pedido_form': pedido_form,
               'detalle_form': detalle_form, 'pedido': pedido}
    return render(request, 'App3/updatepedido.html', context)


def indexpedido(request):
    pedidos = Pedido.objects.all()
    context = {'pedidos': pedidos}
    return render(request, 'App3/indexpedido.html', context)


def deletepedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    DetallePedido.objects.filter(pedido=pedido).delete()

    pedido.delete()

    return redirect('indexpedido')
