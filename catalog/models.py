from django.db import models
from django.conf import settings

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
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="цена за покупку"
    )
    #  НОВОЕ ПОЛЕ: Статус публикации (Задание 1)
    is_published = models.BooleanField(
        default=False,
        verbose_name="опубликовано"
    )
    # НОВОЕ ПОЛЕ: Владелец (Задание 2)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  #  CustomUser из users
        on_delete=models.CASCADE,
        verbose_name="владелец",
        related_name='products'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата последнего изменения")

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ["-created_at", "name"]
        #  КАСТОМНЫЕ ПРАВА (Задание 1)
        permissions = [
            ('can_unpublish_product', 'Может отменять публикацию продукта'),
        ]

    def __str__(self):
        return f"{self.name} - {self.price} руб."
