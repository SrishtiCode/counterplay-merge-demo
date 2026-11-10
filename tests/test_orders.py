import pytest

from shop.orders import Line, line_total, order_total


def test_line_total():
    assert line_total(Line("pen", 150, 4)) == 600
    with pytest.raises(ValueError):
        line_total(Line("pen", 150, 0))


def test_order_total():
    lines = [Line("pen", 150, 4), Line("book", 1200)]
    # 1800, minus 10 % = 1620, plus 20 % tax = 1944.
    assert order_total(lines, discount_percent=10) == 1944
