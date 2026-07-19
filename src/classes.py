from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """Базовый абстрактный класс для всех продуктов"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class PrintMixin:
    """Миксин для логирования создания объекта"""

    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        # Собираем все значения атрибутов из __dict__
        params = ", ".join([f"{repr(value)}" for value in self.__dict__.values() if not value.__class__.__name__ == 'bool'])
        # Если в __dict__ есть приватные атрибуты, они будут с именем класса, это нормально для лога
        return f"{self.__class__.__name__}({params})"

class Product(PrintMixin, BaseProduct):
    """Класс описания продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        # Вызываем инициализатор миксина
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) == type(other):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        raise TypeError

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data.get("name"),
            description=product_data.get("description"),
            price=product_data.get("price"),
            quantity=product_data.get("quantity"),
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

class Smartphone(Product):
    """Класс Смартфон"""
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

class LawnGrass(Product):
    """Класс Трава газонная"""
    def __init__(self, name, description, price, quantity, country, period, color):
        self.country = country
        self.period = period
        self.color = color
        super().__init__(name, description, price, quantity)

class Category:
    """Класс описания продуктов внутри одной категории"""
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, new_product):
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        return "\n".join([str(p) for p in self.__products])
