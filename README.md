# SkyStore - Интернет-магазин

## Описание
SkyStore - это интернет-магазин для продажи плагинов, рассылок, ботов и утилит.

## Установка
1. Создайте виртуальное окружение: `python -m venv venv`
2. Активируйте его: `source venv/bin/activate` (Linux/Mac) или `venv\Scripts\activate` (Windows)
3. Установите зависимости: `pip install -r requirements.txt` или `poetry install`
4. Запустите миграции: `python manage.py migrate`
5. Запустите сервер: `python manage.py runserver`

## Структура
- `catalog/` - приложение каталога с главной и страницей контактов
- `static/` - статические файлы (CSS, JS, изображения)
- `templates/` - шаблоны HTML

## Использованные технологии
- Django 4.x
- Bootstrap 5
- Python 3.x
