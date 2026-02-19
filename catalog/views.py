from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from .forms import ProductForm


# Твои views остаются БЕЗ ИЗМЕНЕНИЙ!
class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    queryset = Product.objects.all()[:5]


class ContactView(TemplateView):
    template_name = 'contact.html'


class CatalogView(ListView):
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'products'
    paginate_by = 12


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'


# CRUD - ИДЕАЛЬНЫ!
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:catalog')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete_confirm.html'
    success_url = reverse_lazy('catalog:catalog')
