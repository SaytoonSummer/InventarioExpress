"""
URL configuration for InventarioExpress project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from App.views import index, updateproduct, deleteproduct, createproduct
from App2.views import userRegistrationView, lista_clientes, eliminarCliente, actualizarCliente
from App3.views import indexpedido, createpedido, deletepedido, updatepedido

urlpatterns = [
    # Direcciones App
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('updateproduct/<int:producto_id>/',
         updateproduct, name='updateproduct'),
    path('deleteproduct/<int:producto_id>/',
         deleteproduct, name='deleteproduct'),
    path('createproduct/', createproduct, name='createproduct'),

    # Direcciones App2
    path('indexcliente/', lista_clientes, name='indexcliente'),
    path('registrar/', userRegistrationView),
    path('eliminar/<int:id>', eliminarCliente),
    path('actualizar/<int:id>', actualizarCliente),

    # Direciones App3

    path('indexpedido/', indexpedido, name='indexpedido'),
    path('createpedido/', createpedido, name='createpedido'),
    path('deletepedido/<int:pedido_id>/', deletepedido, name='deletepedido'),
    path('updatepedido/<int:pedido_id>/', updatepedido, name='updatepedido'),

    # Direcciones API

    path('api/', include('api_app.urls')),
]
