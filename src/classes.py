class Product:
    """Класс описания продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is self.__class__:
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        raise TypeError

    @classmethod
    def new_product(cls, product_data: dict):
        """Создает и возвращает новый объект Product из словаря"""
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
    def price(self, new_price) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

class Category:
    """Класс описания продуктов внутри одной категории"""

    name: str
    description: str
    products: list
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

    def add_product(self, new_product: Product):
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        result = []
        for product in self.__products:
            result.append(str(product))
        return "\n".join(result)

class Smartphone(Product):
    """Класс продукта 'Смартфон'"""

    efficiency: str
    model: str
    memory: str
    color: str

    def __init__(
        self,
        name,
        description,
        price,
        quantity,
        efficiency,
        model,
        memory,
        color,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product):
    """Класс продукта 'трава газонная'"""

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name,
        description,
        price,
        quantity,
        country,
        germination_period,
        color,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
