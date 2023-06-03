from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import *


class ProductsView(ListView):
    model = Products
    context_object_name = 'products'
    template_name = 'products/products.html'


class CategoriesView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'categories/category.html'


class OrderView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'order/order.html'


class ProductCreateView(CreateView):
    model = Products
    form_class = ProductForm
    template_name = 'products/add-product.html'
    success_url = 'all-products'


class OrderFormView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'products/prod-detail.html'
    success_url = 'all-products'


class ProductsDetailView(DetailView):
    model = Products
    context_object_name = 'product'
    template_name = 'products/prod-detail.html'
