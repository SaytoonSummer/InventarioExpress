from django.shortcuts import render, redirect
from django.http import HttpResponse
from App2.models import Cliente
from App2.forms import FormCliente
from . import forms

# Create your views here.


def lista_clientes(request):
    clientes = Cliente.objects.all()
    data = {'clientes': clientes}
    return render(request, 'App2/indexcliente.html', data)


def userRegistrationView(request):
    form = forms.FormCliente()

    if request.method == 'POST':
        form = forms.FormCliente(request.POST)
        if form.is_valid():
            print("Nombre: ", form.cleaned_data['nombre'])
            print("correo", form.cleaned_data['correo'])
            print("direccion", form.cleaned_data['direccion'])
            print("telefono", form.cleaned_data['telefono'])
            print("tipoCliente", form.cleaned_data['tipoCliente'])
            form.save()
            return redirect('indexcliente')

        else:
            print("Formulario inválido")

    data = {'form': form}
    return render(request, 'App2/registrar.html', data)


def eliminarCliente(request, id):
    cliente = Cliente.objects.get(idCliente=id)
    cliente.delete()
    return redirect('indexcliente')


def actualizarCliente(request, id):
    cliente = Cliente.objects.get(idCliente=id)
    form = FormCliente(instance=cliente)
    if request.method == 'POST':
        form = FormCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
        return redirect('indexcliente')
    data = {'form': form}
    return render(request, 'App2/registrar.html', data)
