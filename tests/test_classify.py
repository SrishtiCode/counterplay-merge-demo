from shop.classify import classify_order


def test_invalid():
    assert classify_order(0, 1, "US", False) == "invalid"
    assert classify_order(100, 0, "US", False) == "invalid"


def test_domestic():
    assert classify_order(100000, 1, "US", True) == "domestic-express-priority"
    assert classify_order(500, 11, "US", True) == "domestic-express-bulk"
    assert classify_order(500, 1, "US", True) == "domestic-express"
    assert classify_order(100000, 1, "US", False) == "domestic-priority"
    assert classify_order(500, 11, "US", False) == "domestic-bulk"
    assert classify_order(500, 1, "US", False) == "domestic"


def test_regional():
    assert classify_order(500, 11, "CA", True) == "regional-express-bulk"
    assert classify_order(500, 1, "MX", True) == "regional-express"
    assert classify_order(50000, 1, "CA", False) == "regional-priority"
    assert classify_order(500, 1, "CA", False) == "regional"


def test_international():
    assert classify_order(500, 1, "DE", True) == "international-express"
    assert classify_order(50000, 1, "DE", False) == "international-priority"
    assert classify_order(500, 1, "DE", False) == "international"
