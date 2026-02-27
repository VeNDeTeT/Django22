from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from .models import Product
from .forms import ProductForm


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(is_published=True)[:5]  #


class ContactView(TemplateView):
    template_name = 'contact.html'


class CatalogView(ListView):
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'products'
    paginate_by = 12
    queryset = Product.objects.filter(is_published=True)

    def get_queryset(self):
        # Получаем номер страницы
        page_number = self.request.GET.get('page', 1)
        cache_key = f'catalog_page_{page_number}'

        # Проверяем кеш
        products = cache.get(cache_key)
        if products is None:
            # Запрос к БД только при MISS
            products = Product.objects.filter(
                is_published=True
            ).select_related('category', 'owner')[
                       :self.paginate_by * 2  # Немного больше для пагинации
                       ]
            cache.set(cache_key, products, 60 * 5)  #  5 минут
        return products


#  CRUD с автопривязкой владельца
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:catalog')

    def form_valid(self, form):
        form.instance.owner = self.request.user  #  Автовладелец
        form.instance.is_published = False  #  Не опубликован по умолчанию
        messages.success(self.request, 'Продукт создан! Опубликуйте через админку.')
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'

    def get_queryset(self):
        #  Только свои продукты
        return Product.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_delete_confirm.html'
    success_url = reverse_lazy('catalog:catalog')

    def get_queryset(self):

        return Product.objects.filter(owner=self.request.user)


#  МОДЕРАТОР: Снятие с публикации (Задание 1.4)
class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Только модератор может снять продукт с публикации (can_unpublish_product)
    """
    model = Product
    fields = []  # Без формы редактирования
    template_name = 'product_unpublish_confirm.html'
    permission_required = 'catalog.can_unpublish_product'
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        self.object.is_published = False
        self.object.save()
        messages.success(
            self.request,
            f' Продукт "{self.object.name}" снят с публикации!'
        )
        return redirect('catalog:catalog')


class CategoryView(ListView):
    template_name = 'category.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        from .services import get_products_by_category
        category_slug = self.kwargs['slug']
        return get_products_by_category(category_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_slug'] = self.kwargs['slug']
        return context