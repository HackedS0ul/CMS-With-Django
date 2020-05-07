from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Item



class ItemList(ListView):
    model = Item
    template_name = 'cms/index.html'


class ProductDetailView(DetailView):
    model = Item
    template_name = 'cms/product.html'


