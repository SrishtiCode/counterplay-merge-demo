import pytest

from shop.orders import Line, classify_order, line_total, order_total


def test_line_total():
    assert line_total(Line("pen", 150, 4)) == 600
    with pytest.raises(ValueError):
        line_total(Line("pen", 150, 0))


def test_order_total():
    lines = [Line("pen", 150, 4), Line("book", 1200)]
    # 1800, minus 10 % = 1620, plus 18 % tax = 1911.
    assert order_total(lines, discount_percent=10) == 1911


def test_classify_order():
    tv, desk = Line("tv", 200_000), Line("desk", 20_000)
    book, pen = Line("book", 5_000), Line("pen", 150)
    bulk = [Line("pen", 2_000)] * 6
    assert classify_order([], "IN", False) == "empty"
    assert classify_order([tv], "IN", True) == "vip-express-domestic"
    assert classify_order([tv], "US", True) == "vip-express-americas"
    assert classify_order([tv], "FR", True) == "vip-express-international"
    assert classify_order([tv], "IN", False) == "vip-domestic"
    assert classify_order([tv], "FR", False) == "vip-international"
    assert classify_order(bulk, "IN", True) == "large-express-bulk"
    assert classify_order([desk], "IN", True) == "large-express"
    assert classify_order(bulk, "IN", False) == "large-bulk"
    assert classify_order([desk], "IN", False) == "large"
    assert classify_order([book], "IN", True) == "medium-express"
    assert classify_order([book], "IN", False) == "medium"
    assert classify_order([pen], "IN", True) == "small-express"
    assert classify_order([pen], "IN", False) == "small"
