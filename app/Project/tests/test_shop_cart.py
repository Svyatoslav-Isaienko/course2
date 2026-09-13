import pytest

from shop_cart import ShoppingCart


class TestShoppingCart:

    @pytest.fixture
    def cart(self) -> ShoppingCart:
        return ShoppingCart()

    def test_init_creates_empty_items_list(self, cart: ShoppingCart):
        assert cart.items == []

    def test_add_new_item(self, cart: ShoppingCart):
        cart.add_item('apple', 10, 2)

        assert cart.items == [{'name': 'apple', 'price': 10, 'quantity': 2}]

    def test_add_several_different_items(self, cart: ShoppingCart):
        cart.add_item('apple', 10, 2)
        cart.add_item('banana', 5, 3)

        assert cart.items == [
            {'name': 'apple', 'price': 10, 'quantity': 2},
            {'name': 'banana', 'price': 5, 'quantity': 3},
        ]

    def test_add_existing_item_sums_quantity_and_overwrites_price(self, cart: ShoppingCart):
        cart.add_item('apple', 10, 2)
        cart.add_item('apple', 12, 3)

        assert cart.items == [{'name': 'apple', 'price': 12, 'quantity': 5}]

    def test_remove_existing_item(self, cart: ShoppingCart):
        cart.add_item('apple', 10, 2)
        cart.add_item('banana', 5, 3)

        cart.remove_item('apple')

        assert cart.items == [{'name': 'banana', 'price': 5, 'quantity': 3}]

    def test_remove_nonexistent_item_does_nothing(self, cart: ShoppingCart):
        cart.add_item('apple', 10, 2)

        cart.remove_item('banana')

        assert cart.items == [{'name': 'apple', 'price': 10, 'quantity': 2}]

    def test_get_total_empty_cart(self, cart: ShoppingCart):
        assert cart.get_total() == 0

    def test_get_total_single_item(self, cart: ShoppingCart):
        cart.add_item('apple', 10, 2)

        assert cart.get_total() == 20

    def test_get_total_multiple_items(self, cart: ShoppingCart):
        cart.add_item('apple', 10, 2)
        cart.add_item('banana', 5, 3)

        assert cart.get_total() == 35

    def test_get_total_after_update_and_removal(self, cart: ShoppingCart):
        cart.add_item('apple', 10, 2)
        cart.add_item('apple', 12, 3)
        cart.add_item('banana', 5, 4)
        cart.remove_item('banana')

        assert cart.get_total() == 60
