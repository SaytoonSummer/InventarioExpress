from django import forms
from django.core import validators
from App2.models import Cliente


class ClienteRegistrationForm(forms.Form):

    ELEGIR_TIPO = [('regular', 'Regular'), ('premium', 'Premium'),
                   ('empresarial', 'Empresarial')]

    nombre = forms.CharField()
    correo = forms.EmailField(validators=[validators.EmailValidator()])
    direccion = forms.CharField(validators=[validators.MinLengthValidator(5)])
    telefono = forms.CharField()
    tipoCliente = forms.CharField(widget=forms.Select(choices=ELEGIR_TIPO))


def clean_nombre(self):
    inputNombre = self.cleaned_data['nombre']
    if len(inputNombre) < 5:
        raise forms.ValidationError(
            "El nombre que introdujo debe tener más de 5 letras.")
    return inputNombre


class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
