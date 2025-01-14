import pytest
from pathlib import Path
import json
from src.utils import read_json, convert_to_objects
from src.models import Product, Category


@pytest.fixture
def sample_json_file(tmp_path):
    """Создаёт временный JSON-файл с примерными данными."""
    file_path = tmp_path / "sample.json"
    data = [
        {
            "name": "Смартфоны",
            "description": "Категория смартфонов",
            "products": [
                {
                    "name": "Samsung Galaxy S23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8
                }
            ]
        },
        {
            "name": "Телевизоры",
            "description": "Категория телевизоров",
            "products": [
                {
                    "name": "55\" QLED 4K",
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7
                }
            ]
        }
    ]
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return file_path


def test_read_json_valid_file(sample_json_file):
    """Тестирование read_json с корректным JSON-файлом."""
    data = read_json(sample_json_file)
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["name"] == "Смартфоны"


def test_read_json_missing_file():
    """Тестирование read_json с отсутствующим файлом."""
    non_existent_path = Path("non_existent.json")
    data = read_json(non_existent_path)
    assert data == []


def test_read_json_invalid_json(tmp_path):
    """Тестирование read_json с некорректным JSON."""
    invalid_file = tmp_path / "invalid.json"
    with open(invalid_file, "w", encoding="utf-8") as f:
        f.write("{invalid json")
    data = read_json(invalid_file)
    assert data == []


def test_convert_to_objects_valid_data():
    """Тестирование convert_to_objects с корректными данными."""
    sample_data = [
        {
            "name": "Смартфоны",
            "description": "Категория смартфонов",
            "products": [
                {
                    "name": "Samsung Galaxy S23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8
                }
            ]
        },
        {
            "name": "Телевизоры",
            "description": "Категория телевизоров",
            "products": [
                {
                    "name": "55\" QLED 4K",
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7
                }
            ]
        }
    ]
    categories = convert_to_objects(sample_data)
    assert isinstance(categories, list)
    assert len(categories) == 2

    first_category = categories[0]
    assert isinstance(first_category, Category)
    assert first_category.name == "Смартфоны"
    assert len(first_category.products) == 2

    first_product = first_category.products[0]
    assert isinstance(first_product, Product)
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_convert_to_objects_empty_data():
    """Тестирование convert_to_objects с пустым списком."""
    categories = convert_to_objects([])
    assert categories == []


def test_convert_to_objects_missing_product_key():
    """Тестирование convert_to_objects с отсутствием ключа products."""
    invalid_data = [
        {
            "name": "Смартфоны",
            "description": "Категория смартфонов"
        }
    ]
    with pytest.raises(KeyError):
        convert_to_objects(invalid_data)
