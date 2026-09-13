class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, name: str, price: float, quantity: int) -> None:
        for item in self.items:
            if item['name'] == name:
                item['quantity'] += quantity
                item['price'] = price
                return

        self.items.append({'name': name, 'price': price, 'quantity': quantity})

    def remove_item(self, name: str) -> None:
        for item in self.items:
            if item['name'] == name:
                self.items.remove(item)
                return

    def get_total(self) -> float:
        return sum(item['price'] * item['quantity'] for item in self.items)
