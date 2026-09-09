def calculate_discount(price: float, discount: float) -> float:
    final_price = price - (price * discount / 100)
    return final_price


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_full_name(first_name: str, last_name: str) -> str:
    full_name = f"{first_name} {last_name}"
    return full_name
