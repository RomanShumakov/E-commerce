import pytest

from src.classes import Category, Product, Smartphone, LawnGrass


@pytest.fixture
def product_iphone():
    return Product("Iphone 17 Pro Max", "512GB, Orange", 210000.0, 7)


@pytest.fixture
def category_smartphones(product_iphone):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_iphone],
    )


@pytest.fixture
def smartphone_1():
    return Smartphone("Iphone 15", "512GB", 210000.0, 8, "super effective", "IPhone", "512GB", "Gray space")

@pytest.fixture
def smartphone_2():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, 200MP камера", 180000.0, 5, "effective", "Samsung", "256GB", "Серый цвет")

@pytest.fixture
def lawngrass_1():
    return LawnGrass("grass", "трава для садоводства", 500, 30, "Russia", "1 month", "green")

@pytest.fixture
def lawngrass_2():
    return LawnGrass("grass", "трава для садоводства", 500, 30, "USA", "10 years", "sky blue")


