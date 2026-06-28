import json
import os

from src.classes import Product, Category

def read_json(path: str) -> list:

    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data

def create_objects_from_json(data):
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    categorise_data = create_objects_from_json(raw_data)
    print(categorise_data[0].name)
    print(categorise_data[0].description)
    print(categorise_data[0].products)
    print(categorise_data[0].products[0].name)
    print(categorise_data[0].products[1].name)
    print(categorise_data[0].products[2].name)
