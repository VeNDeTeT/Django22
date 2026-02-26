from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Создаём группу
        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Кастомное разрешение
        content_type = ContentType.objects.get_for_model(Product)
        permission = Permission.objects.get_or_create(
            codename='can_unpublish_product',
            name='Может отменять публикацию продукта',
            content_type=content_type,
        )[0]
        group.permissions.add(permission)

        # Стандартные права удаления
        delete_perm = Permission.objects.get(
            codename='delete_product',
            content_type=content_type
        )
        group.permissions.add(delete_perm)

        self.stdout.write(
            self.style.SUCCESS('Группа "Модератор продуктов" создана!')
        )
