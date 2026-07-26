import json
from unittest.mock import mock_open, patch

from src.classes import Category
from src.utils import create_objects_from_json, read_json


def test_read_json():
    """Тестируем чтение JSON-файла с использованием мока"""
    mock_data = [{"name": "Test Category", "description": "Test Desc", "products": []}]
    mock_json = json.dumps(mock_data)

    # Подменяем функцию open, чтобы она не лезла на диск, а возвращала наш mock_json
    with patch("builtins.open", mock_open(read_data=mock_json)):
        result = read_json("fake_path.json")
        assert result == mock_data


def test_create_objects_from_json():
    """Тестируем преобразование списка словарей в объекты классов"""
    sample_data = [
        {
            "name": "Смартфоны",
            "description": "Описание",
            "products": [{"name": "Samsung", "description": "256GB", "price": 100.0, "quantity": 5}],
        }
    ]
    categories = create_objects_from_json(sample_data)

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Смартфоны"
    assert "Samsung" in categories[0].products
