from django.views.generic import ListView, DetailView, TemplateView
from .models import Product

class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    queryset = Product.objects.all()[:5]

class ContactView(TemplateView):
    template_name = 'contact.html'

class CatalogView(ListView):
    model = Product
    template_name = 'catalog.html'  # ← ИСПРАВЛЕНО!
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'
