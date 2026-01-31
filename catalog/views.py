from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {'products': products})

def contact(request):
    return render(request, "contact.html")

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {'product': product})

def catalog(request):
    products = Product.objects.all()
    return render(request, "catalog.html", {'products': products})
