from django.shortcuts import render
from .models import Products
from django.shortcuts import get_object_or_404


def index(request):
    products = Products.objects.all()
    return render(request, 'products/index.html', {'products': products})


def detail(request, pk):
    products = get_object_or_404(Products, pk=pk)
    return render(request, 'products/detail.html', {'products': products})
