from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator
from django.core.exceptions import ValidationError
from .models import Producto


class NoNumbersValidator:
    def __call__(self, value):
        if any(char.isdigit() for char in value):
            raise ValidationError("Este campo no puede contener números.")


class ProductoForm(forms.ModelForm):
    precio = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        validators=[
            MinValueValidator(
                0.01, message="El precio debe ser mayor que cero.")
        ]
    )

    stock_disponible = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        validators=[
            MinValueValidator(0, message="El stock no puede ser negativo.")
        ]
    )

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            MinLengthValidator(1, message="Este campo es obligatorio."),
            NoNumbersValidator()
        ]
    )

    descripcion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            MinLengthValidator(1, message="Este campo es obligatorio."),
            NoNumbersValidator()
        ]
    )

    categoria = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            MinLengthValidator(1, message="Este campo es obligatorio."),
            NoNumbersValidator()
        ]
    )

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'fecha_creacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio <= 0:
            raise ValidationError("El precio debe ser mayor que cero.")
        return precio


class DeleteProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'stock_disponible': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'fecha_creacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'readonly': 'readonly'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
