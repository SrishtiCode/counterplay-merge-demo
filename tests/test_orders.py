import pytest

from shop.orders import Line, format_line, line_total, order_total


def test_line_total():
    assert line_total(Line("pen", 150, 4)) == 600
    with pytest.raises(ValueError):
        line_total(Line("pen", 150, 0))


def test_format_line():
    assert format_line(Line("pen", 150, 4)) == "pen x4 €6.00"
    assert format_line(Line("book", 1205)) == "book x1 €12.05"
    with pytest.raises(ValueError):
        format_line(Line("pen", 150, 0))


def test_order_total():
    lines = [Line("pen", 150, 4), Line("book", 1200)]
    # 1800, minus 10 % = 1620, plus 18 % tax = 1911.
    assert order_total(lines, discount_percent=10) == 1911
