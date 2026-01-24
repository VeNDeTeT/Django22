from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Добавляет тестовые товары в базу (удаляет старые)'

    def handle(self, *args, **options):
        print("=" * 50)
        print("🚀 НАЧАЛО: Заполнение базы тестовыми данными")
        print("=" * 50)

        # 1. Удаляем все старые данные
        print("\n1. Удаление старых данных...")
        Product.objects.all().delete()
        Category.objects.all().delete()
        print("   ✅ Старые данные удалены")

        # 2. Создаем категории
        print("\n2. Создание категорий...")

        cat1 = Category.objects.create(
            name="Электроника",
            description="Техника и гаджеты"
        )
        print(f"   ✅ Категория: {cat1.name}")

        cat2 = Category.objects.create(
            name="Одежда",
            description="Одежда и обувь"
        )
        print(f"   ✅ Категория: {cat2.name}")

        cat3 = Category.objects.create(
            name="Книги",
            description="Книги и учебники"
        )
        print(f"   ✅ Категория: {cat3.name}")

        # 3. Создаем товары
        print("\n3. Создание товаров...")

        # Электроника
        Product.objects.create(
            name="Смартфон iPhone",
            description="Флагманский смартфон",
            price=89999.99,
            category=cat1
        )
        print("   ✅ Товар: Смартфон iPhone - 89999.99 руб.")

        Product.objects.create(
            name="Ноутбук ASUS",
            description="Игровой ноутбук",
            price=74999.99,
            category=cat1
        )
        print("   ✅ Товар: Ноутбук ASUS - 74999.99 руб.")

        # Одежда
        Product.objects.create(
            name="Футболка",
            description="Хлопковая футболка",
            price=1499.99,
            category=cat2
        )
        print("   ✅ Товар: Футболка - 1499.99 руб.")

        Product.objects.create(
            name="Джинсы",
            description="Классические джинсы",
            price=4999.99,
            category=cat2
        )
        print("   ✅ Товар: Джинсы - 4999.99 руб.")

        # Книги
        Product.objects.create(
            name="Книга по Python",
            description="Учебник по программированию",
            price=1999.99,
            category=cat3
        )
        print("   ✅ Товар: Книга по Python - 1999.99 руб.")

        # 4. Итог
        print("\n" + "=" * 50)
        print("✅ ВСЕ ДАННЫЕ УСПЕШНО СОЗДАНЫ!")
        print("=" * 50)

        # Статистика
        total_categories = Category.objects.count()
        total_products = Product.objects.count()

        print(f"\n📊 СТАТИСТИКА:")
        print(f"   • Категорий: {total_categories}")
        print(f"   • Товаров: {total_products}")

        # Самый дорогой товар
        expensive = Product.objects.order_by('-price').first()
        print(f"   • Самый дорогой: {expensive.name} ({expensive.price} руб.)")

        print("\n" + "=" * 50)
        print("🎉 КОМАНДА ВЫПОЛНЕНА УСПЕШНО!")
        print("=" * 50)