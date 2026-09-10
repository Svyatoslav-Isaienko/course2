from utils_hw import calculate_discount, is_even, get_full_name

def test_calculate_discount_20_percent():
    price = 100
    discount = 20
    expected = 80
    actual = calculate_discount(price, discount)
    assert actual == expected


def test_calculate_discount_50_percent():
    price = 200
    discount = 50
    expected = 100
    actual = calculate_discount(price, discount)
    assert actual == expected


def test_calculate_discount_0_percent():
    price = 150
    discount = 0
    expected = 150
    actual = calculate_discount(price, discount)
    assert actual == expected


def test_calculate_discount_zero_price():
    price = 0
    discount = 30
    expected = 0
    actual = calculate_discount(price, discount)
    assert actual == expected


def test_calculate_discount_100_percent():
    price = 500
    discount = 100
    expected = 0
    actual = calculate_discount(price, discount)
    assert actual == expected


def test_is_even_positive_even_number():
    number = 8
    expected = True
    actual = is_even(number)
    assert expected is actual


def test_is_even_positive_odd_number():
    number = 7
    expected = False
    actual = is_even(number)
    assert expected is actual


def test_is_even_negative_even_number():
    number = -4
    expected = True
    actual = is_even(number)
    assert expected is actual


def test_is_even_negative_odd_number():
    number = -3
    expected = False
    actual = is_even(number)
    assert expected is actual


def test_is_even_zero():
    number = 0
    expected = True
    actual = is_even(number)
    assert expected is actual



def test_get_full_name_regular():
    first_name = "Ivan"
    last_name = "Petrenko"
    expected = "Ivan Petrenko"
    actual = get_full_name(first_name, last_name)
    assert actual == expected


def test_get_full_name_short_first_name():
    first_name = "Yo"
    last_name = "Kovalenko"
    expected = "Yo Kovalenko"
    actual = get_full_name(first_name, last_name)
    assert actual == expected


def test_get_full_name_long_first_name():
    first_name = "Maximilian"
    last_name = "Shevchenko"
    expected = "Maximilian Shevchenko"
    actual = get_full_name(first_name, last_name)
    assert actual == expected


def test_get_full_name_single_character():
    first_name = "A"
    last_name = "B"
    expected = "A B"
    actual = get_full_name(first_name, last_name)
    assert actual == expected


def test_get_full_name_with_hyphenated_last_name():
    first_name = "Olena"
    last_name = "Kravets-Boyko"
    expected = "Olena Kravets-Boyko"
    actual = get_full_name(first_name, last_name)
    assert actual == expected
