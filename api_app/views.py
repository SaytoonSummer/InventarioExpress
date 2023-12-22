from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PedidoSerializer, DetallePedidoSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'productos': reverse('productos-list', request=request, format=format),
        'clientes': reverse('clientes-list', request=request, format=format),
        'pedidos': reverse('pedidos-list', request=request, format=format),
    })


@api_view(['POST'])
def crear_pedido(request):
    pedido_serializer = PedidoSerializer(data=request.data)

    if pedido_serializer.is_valid():
        pedido = pedido_serializer.save()

        detalles_data = request.data.get('detalles', [])

        for detalle_data in detalles_data:
            detalle_data['pedido'] = pedido.id
            detalle_serializer = DetallePedidoSerializer(data=detalle_data)

            if detalle_serializer.is_valid():
                detalle_serializer.save()
            else:
                pedido.delete()
                return Response(detalle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(PedidoSerializer(pedido).data, status=status.HTTP_201_CREATED)
    else:
        return Response(pedido_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
