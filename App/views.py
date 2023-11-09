from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm, DeleteProductForm


def index(request):
    productos = Producto.objects.all()
    return render(request, 'App/index.html', {'productos': productos})


def updateproduct(request, producto_id):
    producto = Producto.objects.get(id=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            print("Datos del formulario válidos:", form.cleaned_data)
            form.save()
            print("Producto actualizado correctamente")
            return redirect('index')
        else:
            print("Errores de validación:", form.errors)
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'App/updateproduct.html', {'form': form})


def deleteproduct(request, producto_id):
    producto = Producto.objects.get(id=producto_id)

    if request.method == 'POST':
        producto.delete()
        return redirect('index')
    else:
        form = DeleteProductForm(instance=producto)

    return render(request, 'App/deleteproduct.html', {'form': form, 'producto': producto})


def createproduct(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()

    return render(request, 'App/createproduct.html', {'form': form})
