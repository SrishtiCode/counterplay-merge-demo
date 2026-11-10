import pytest

from shop.pricing import apply_discount, format_price, with_tax


def test_format_price():
    assert format_price(1250) == "€12.50"
    assert format_price(5) == "€0.05"
    assert format_price(-300) == "-€3.00"


def test_apply_discount():
    assert apply_discount(1000, 10) == 900
    assert apply_discount(999, 50) == 499
    with pytest.raises(ValueError):
        apply_discount(1000, 120)


def test_with_tax():
    assert with_tax(1000) == 1200
