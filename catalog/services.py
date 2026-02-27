from .models import Product


def get_products_by_category(category_slug):
    """
    Сервис: продукты по категории (кешируем!)
    """
    from django.core.cache import cache

    cache_key = f'products_category_{category_slug}'
    products = cache.get(cache_key)

    if products is None:
        products = Product.objects.filter(
            category__slug=category_slug,
            is_published=True
        )
        cache.set(cache_key, products, 60 * 30)  # 30 мин
    return products
