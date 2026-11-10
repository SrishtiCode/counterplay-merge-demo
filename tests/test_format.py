from shop.format import format_price


def test_format_price():
    assert format_price(0) == "$0.00"
    assert format_price(5) == "$0.05"
    assert format_price(1911) == "$19.11"
    assert format_price(123450) == "$1,234.50"


def test_format_price_negative_and_symbol():
    assert format_price(-5) == "-$0.05"
    assert format_price(1200, symbol="€") == "€12.00"
