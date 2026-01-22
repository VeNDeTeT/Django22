from django.db import models


class Category(models.Model):
    """
    Модель Category (Категория)
    """

    name = models.CharField(max_length=150, verbose_name="наименование")
    description = models.TextField(verbose_name="описание", blank=True, null=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]  # сортировка по имени

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Модель Product (Товар)
    """

    name = models.CharField(max_length=150, verbose_name="наименование")
    description = models.TextField(verbose_name="описание", blank=True, null=True)
    image = models.ImageField(
        upload_to="products/", verbose_name="изображение", blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="категория",
        blank=True,
        null=True,
        related_name="products",  # позволяет получать товары категории через category.products
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="цена за покупку"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="дата последнего изменения"
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ["-created_at", "name"]  # сначала новые, потом по имени

    def __str__(self):
        return f"{self.name} - {self.price} руб."
