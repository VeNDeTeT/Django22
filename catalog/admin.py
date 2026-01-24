from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админка для категорий"""

    list_display = ("id", "name")  # Отображение id и name в списке
    list_display_links = ("name",)  # Ссылка на редактирование через name
    search_fields = ("name", "description")  # Поиск по name и description


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка для товаров"""

    list_display = ("id", "name", "price", "category")  # Отображение в списке
    list_display_links = ("name",)  # Ссылка на редактирование через name
    list_filter = ("category",)  # Фильтрация по категории
    search_fields = ("name", "description")  # Поиск по name и description
    list_editable = ("price",)  # Цену можно редактировать прямо в списке
    list_per_page = 20  # Пагинация: 20 товаров на странице

    # Опционально: группировка полей в форме редактирования
    fieldsets = (
        (
            "Основная информация",
            {"fields": ("name", "description", "category", "price")},
        ),
        ("Изображение", {"fields": ("image",), "classes": ("collapse",)}),
        ("Даты", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )

    # Поля только для чтения (даты)
    readonly_fields = ("created_at", "updated_at")
