def test_product_init(product_iphone):
    assert product_iphone.name == "Iphone 17 Pro Max"
    assert product_iphone.description == "512GB, Orange"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 7


def test_category_init(category_smartphones):
    assert category_smartphones.name == "Смартфоны"
    assert (
        category_smartphones.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_smartphones.products == ["product1", "product2", "product3"]
    assert category_smartphones.product_count == 3
    assert category_smartphones.category_count == 1
