import pytest

from shopping_cart import ShoppingCart


@pytest.fixture
def cart() -> ShoppingCart:
    return ShoppingCart()


@pytest.fixture
def default_item() -> dict:
    return {'name': 'apple', 'price': 10, 'quantity': 2}


@pytest.fixture
def cart_with_default_item(cart: ShoppingCart, default_item: dict) -> ShoppingCart:
    cart.add_item(default_item['name'], default_item['price'], default_item['quantity'])
    return cart