import pytest

from src.classes import Category, Product


@pytest.fixture
def product_iphone():
    return Product("Iphone 17 Pro Max", "512GB, Orange", 210000.0, 7)


@pytest.fixture
def category_smartphones():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        ["product1", "product2", "product3"],
    )
