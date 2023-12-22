# En api_app/urls.py
from .views import api_root, crear_pedido
from django.urls import path
from .views import api_root
from rest_framework import routers
from .api import ProductoViewSet, ClienteViewSet, PedidoViewSet

router = routers.DefaultRouter()
router.register('productos', ProductoViewSet, 'productos')
router.register('clientes', ClienteViewSet, 'clientes')
router.register('pedidos', PedidoViewSet, 'pedidos')

urlpatterns = [
    path('', api_root, name='api-root'),
    path('api/pedidos/crear/', crear_pedido,
         name='crear-pedido'),
    *router.urls,
]
