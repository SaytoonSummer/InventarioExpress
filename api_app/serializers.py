# En api_app/serializers.py
from rest_framework import serializers
from App.models import Producto
from App2.models import Cliente
from App3.models import Pedido, DetallePedido


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'descripcion', 'precio',
                  'stock_disponible', 'fecha_creacion', 'categoria')
        read_only_fields = ('fecha_creacion', )


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class DetallePedidoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = DetallePedido
        fields = ('id', 'producto', 'cantidad', 'pedido')


class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many=True, read_only=True)

    productos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Producto.objects.all())

    cantidad = serializers.IntegerField(write_only=True)

    class Meta:
        model = Pedido
        fields = ('id', 'fecha', 'estado', 'metodo_pago', 'direccion_entrega',
                  'total_pedido', 'cliente', 'productos', 'cantidad', 'detalles')

    def create(self, validated_data):
        cantidad = validated_data.pop('cantidad', None)
        productos = validated_data.pop('productos', [])

        pedido = Pedido.objects.create(**validated_data)

        for producto in productos:
            DetallePedido.objects.create(
                pedido=pedido, producto=producto, cantidad=cantidad)

        return pedido
