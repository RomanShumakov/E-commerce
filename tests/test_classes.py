import pytest

from src.classes import BaseProduct, LawnGrass, Product, Smartphone, Category


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


def test_smartphone_init(smartphone_1):
    """Проверка инииализации класса Smartphone"""
    assert smartphone_1.name == "Iphone 15"
    assert smartphone_1.description == "512GB"
    assert smartphone_1.price == 210000.0
    assert smartphone_1.quantity == 8
    assert smartphone_1.efficiency == "super effective"
    assert smartphone_1.model == "IPhone"
    assert smartphone_1.memory == "512GB"
    assert smartphone_1.color == "Gray space"


def test_smartphone_sum(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 210000.0 * 8 + 180000.0 * 5


def test_smartphone_sum_error(smartphone_1):
    with pytest.raises(TypeError):
        result = smartphone_1 + 1


def test_lawngrass_init(lawngrass_1):
    """Проверка инииализации класса Smartphone"""
    assert lawngrass_1.name == "grass"
    assert lawngrass_1.description == "трава для садоводства"
    assert lawngrass_1.price == 500
    assert lawngrass_1.quantity == 30
    assert lawngrass_1.country == "Russia"
    assert lawngrass_1.germination_period == "1 month"
    assert lawngrass_1.color == "green"


def test_lawngrass_sum(lawngrass_1, lawngrass_2):
    assert lawngrass_1 + lawngrass_2 == 500 * 30 + 500 * 30


def test_lawngrass_sum_error(lawngrass_1):
    with pytest.raises(TypeError):
        result = lawngrass_1 + 1


def test_add_product_success(category_smartphones, smartphone_2):
    """Проверка успешного добавления наследника Product (смартфона) в категорию"""
    # Так как products возвращает строку, считаем количество продуктов по строкам
    initial_count = len(category_smartphones.products.strip().split("\n"))

    # Добавляем новый смартфон
    category_smartphones.add_product(smartphone_2)

    # Теперь строк должно стать на одну больше
    current_count = len(category_smartphones.products.strip().split("\n"))
    assert current_count == initial_count + 1

    # И строковое представление нового смартфона теперь есть внутри этой большой строки
    assert str(smartphone_2) in category_smartphones.products


def test_add_product_invalid_type(category_smartphones):
    """Проверка ошибки при попытке добавить не-Product"""
    with pytest.raises(TypeError):
        category_smartphones.add_product("Просто какая-то строка вместо объекта")


def test_base_product_instantiation():
    """Проверяем, что абстрактный класс BaseProduct нельзя инициализировать напрямую"""
    with pytest.raises(TypeError):
        BaseProduct()


def test_print_mixin_console_output(capsys):
    """Проверяем, что при создании продукта в консоль печатается информация об объекте"""
    # Создаем продукт, миксин должен сработать и напечатать лог в консоль
    product = Product("Тестовый телефон", "Описание", 50000.0, 3)

    captured = capsys.readouterr()

    # Проверяем, что в выводе содержится имя класса и переданные аргументы
    assert "Product" in captured.out
    assert "'Тестовый телефон'" in captured.out
    assert "50000.0" in captured.out


def test_repr_format_for_different_classes():
    """Проверяем, что __repr__ возвращает корректную строку для разных классов"""
    product = Product("Тестовый телефон", "Описание", 50000.0, 3)
    assert repr(product).startswith("Product(")
    assert "'Тестовый телефон'" in repr(product)

    smartphone = Smartphone("Samsung", "S23", 100000.0, 2, "high", "S23", "128", "Black")
    assert repr(smartphone).startswith("Smartphone(")
    assert "'Samsung'" in repr(smartphone)

def test_product_zero_quantity_error():
    """Тестируем перехват ошибки ValueError при создании товара с нулевым количеством"""
    with pytest.raises(ValueError) as excinfo:
        Product("Сломанный телефон", "Описание", 50000.0, 0)
    assert str(excinfo.value) == "Товар с нулевым количеством не может быть добавлен"

def test_category_average_price(category_smartphones):
    """Тестируем средний ценник в категории с товарами"""
    # В category_smartphones из фикстуры уже лежит 1 товар: Iphone 17 Pro Max за 210000.0
    # Добавим второй, чтобы проверить расчет среднего арифметического ценников
    another_phone = Product("Бюджетный телефон", "Описание", 90000.0, 5)
    category_smartphones.add_product(another_phone)

    # Ожидаемое среднее: (210000.0 + 90000.0) / 2 = 150000.0
    assert category_smartphones.average_price() == 150000.0

def test_category_average_price_empty():
    """Тестируем, что для пустой категории метод average_price вернет 0"""
    empty_category = Category("Пустая категория", "У нас тут ничего нет", [])
    assert empty_category.average_price() == 0
