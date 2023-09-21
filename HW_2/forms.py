from django import forms
from HW_2 import models

class CatalogForm(forms.Form):
    name_of_product = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Введите название продукта:'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание продукта:'}))
    price = forms.DecimalField(max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Стоимость:'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Количество:'}))
    image = forms.ImageField()
