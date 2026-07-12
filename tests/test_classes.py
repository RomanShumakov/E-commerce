import pytest
from src.classes import Product

def test_product_init(product_iphone):
    assert product_iphone.name == "Iphone 17 Pro Max"
    assert product_iphone.description == "512GB, Orange"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 7

def test_product_price_setter(product_iphone):
    """Тестируем изменение цены и валидацию"""
    product_iphone.price = 250000.0
    assert product_iphone.price == 250000.0

    # Проверяем, что цена не упадет при вводе некорректного значения
    product_iphone.price = -100
    assert product_iphone.price == 250000.0

def test_product_str(product_iphone):
    """Тестируем строковое отображение продукта"""
    assert str(product_iphone) == "Iphone 17 Pro Max, 210000.0 руб. Остаток: 7 шт."

def test_product_add(product_iphone):
    """Тестируем сложение двух продуктов (__add__)"""
    product_samsung = Product("Samsung Galaxy S24", "256GB", 120000.0, 5)
    # Считаем: (210000 * 7) + (120000 * 5) = 1 470 000 + 600 000 = 2 070 000
    assert product_iphone + product_samsung == 2070000.0

def test_category_init(category_smartphones):
    assert category_smartphones.name == "Смартфоны"
    assert "Iphone 17 Pro Max, 210000.0 руб. Остаток: 7 шт." in category_smartphones.products
    assert category_smartphones.product_count == 1
    assert category_smartphones.category_count == 1

def test_category_str(category_smartphones):
    """Тестируем строковое отображение категории"""
    assert str(category_smartphones) == "Смартфоны, количество продуктов: 7 шт."
