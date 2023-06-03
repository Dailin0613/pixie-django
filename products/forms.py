from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'inStock': forms.CheckboxInput(attrs={'class': 'form-control'})
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']
