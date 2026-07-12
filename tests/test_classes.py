import pytest

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

def test_category_init(category_smartphones):
    assert category_smartphones.name == "Смартфоны"
    assert "Iphone 17 Pro Max, 210000.0 руб. Остаток: 7 шт." in category_smartphones.products
    assert category_smartphones.product_count == 1
    assert category_smartphones.category_count == 1

