import pytest
from src.models import Product, Category


@pytest.fixture
def product_example():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)


@pytest.fixture
def another_product_example():
    return Product("iPhone 15 Pro", "256GB, Черный цвет", 200000.0, 3)


@pytest.fixture
def category_example(product_example, another_product_example):
    return Category(
        "Смартфоны",
        "Категория для современных смартфонов",
        [product_example, another_product_example]
    )


@pytest.fixture
def another_product_example():
    return Product("iPhone 15 Pro", "256GB, Черный цвет", 200000.0, 3)


def test_product_init(product_example):
    """ Тестирование инициализации объекта Product """
    assert product_example.name == "Samsung Galaxy S23 Ultra"
    assert product_example.description == "256GB, Серый цвет"
    assert product_example.price == 180000.0
    assert product_example.quantity == 5


def test_category_init(category_example, product_example, another_product_example):
    """ Тестирование инициализации объекта Category, тест атрибутов """
    assert category_example.name == "Смартфоны"
    assert category_example.description == "Категория для современных смартфонов"

    assert len(category_example.products) == 2
    assert category_example.products[0] == product_example
    assert category_example.products[1] == another_product_example

    assert Category.category_count == 1  # Should be 1 if this is the only test running
    assert Category.product_count == 2   # Reflects the total number of products


def test_category_empty_product_list():
    """ Тестирование Категории с пустым списком продуктов """
    empty_category = Category("Пустая категория", "Нет продуктов", [])
    assert empty_category.name == "Пустая категория"
    assert empty_category.description == "Нет продуктов"
    assert len(empty_category.products) == 0
    assert Category.category_count == 2
    assert Category.product_count == 2
