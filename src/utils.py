import json
from pathlib import Path

from src.models import Category, Product

BASE_DIR = Path(__file__).resolve().parent.parent


def read_json(path: Path) -> list:
    """Получение списка продуктов из файла JSON."""
    if not path.exists():
        return []

    try:
        with open(path, "r", encoding="utf-8") as file:
            products_data = json.load(file)
            return products_data if isinstance(products_data, list) else []
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON.")
        return []
    except IOError:
        print("Ошибка ввода-вывода при чтении файла.")
        return []


def convert_to_objects(data: list) -> list:
    """Преобразование списка категорий и продуктов в объекты Category и Product."""
    categories = []

    for category_data in data:
        products_list = [
            Product(
                name=product["name"],
                description=product["description"],
                price=product["price"],
                quantity=product["quantity"],
            )
            for product in category_data["products"]
        ]

        category = Category(
            name=category_data["name"], description=category_data["description"], products=products_list
        )
        categories.append(category)

    return categories
