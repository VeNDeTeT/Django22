from django.core.cache import cache
from .models import Product


def get_products_by_category(category_pk):
    """
    Сервис: продукты по категории (кешируем!)
    """

    cache_key = f'products_category_pk_{category_pk}'
    products = cache.get(cache_key)

    if products is None:
        products = Product.objects.filter(
            category_id=category_pk,
            is_published=True
        ).order_by('-created_at')
        cache.set(cache_key, products, 60 * 30)  # 30 мин
    return products
