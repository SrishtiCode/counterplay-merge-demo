from shop.format import format_discount, format_price, format_quantity


def test_format_price():
    assert format_price(0) == "$0.00"
    assert format_price(5) == "$0.05"
    assert format_price(1911) == "$19.11"
    assert format_price(123450) == "$1,234.50"


def test_format_price_negative_and_symbol():
    assert format_price(-5) == "-$0.05"
    assert format_price(1200, symbol="€") == "€12.00"


def test_format_quantity():
    assert format_quantity(0) == "0 items"
    assert format_quantity(1) == "1 item"
    assert format_quantity(2) == "2 items"
    assert format_quantity(1200) == "1,200 items"


def test_format_quantity_noun():
    assert format_quantity(1, noun="bag") == "1 bag"
    assert format_quantity(3, noun="order") == "3 orders"


def test_format_discount():
    assert format_discount(10) == "10% off"
    assert format_discount(5) == "5% off"
