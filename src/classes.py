from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для продуктов"""

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        pass

    @abstractmethod
    def __str__(self):
        pass


class PrintMixin:
    """Миксин для логирования создания объекта"""

    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        # Собираем значения всех атрибутов из __dict__
        params = [repr(v) for v in self.__dict__.values()]
        return f"{self.__class__.__name__}({', '.join(params)})"


class Product(PrintMixin, BaseProduct):
    """Класс описания продукта"""

    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного класса")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product_data):
        return cls(**product_data)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value


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

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)


class Category:
    """Класс категории товаров"""

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Добавлять можно только объекты Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return "\n".join([str(p) for p in self.__products])

    def __len__(self):
        # Возвращаем общее количество штук товаров в категории
        return sum(p.quantity for p in self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."
