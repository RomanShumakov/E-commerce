class Product:
    """Класс описания продукта"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс описания продуктов внутри одной категории"""
    name: str
    description: str
    products: list
    count_of_categories = 0
    count_of_sales = 0


    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.count_of_categories += 1
        Category.count_of_sales += len(products)
