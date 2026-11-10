from datetime import date

import pytest

from shop.discounts import CODES, DiscountError, apply_discount, discount_cents, find_discount

TODAY = date(2026, 11, 10)


def test_save10_takes_ten_percent():
    assert apply_discount(5000, "SAVE10", TODAY) == 4500
    assert apply_discount(999, "SAVE10", TODAY) == 900


def test_welcome5_over_twenty_euros():
    assert apply_discount(2001, "WELCOME5", TODAY) == 1501
    assert apply_discount(5000, "WELCOME5", TODAY) == 4500


def test_welcome5_not_at_or_under_twenty_euros():
    assert apply_discount(2000, "WELCOME5", TODAY) == 2000
    assert apply_discount(1000, "WELCOME5", TODAY) == 1000


def test_code_is_case_and_space_insensitive():
    assert apply_discount(5000, " save10 ", TODAY) == 4500


def test_unknown_code_refused():
    with pytest.raises(DiscountError, match="Unknown discount code"):
        apply_discount(5000, "FREE100", TODAY)


def test_expired_code_refused():
    expired = date(2028, 1, 1)
    with pytest.raises(DiscountError, match="expired on 2027-06-30"):
        apply_discount(5000, "SAVE10", expired)
    with pytest.raises(DiscountError, match="expired on 2027-12-31"):
        apply_discount(5000, "WELCOME5", expired)


def test_code_valid_on_expiry_day():
    assert find_discount("SAVE10", date(2027, 6, 30)) == CODES["SAVE10"]


def test_discount_never_exceeds_total():
    assert discount_cents(CODES["WELCOME5"], 2001) == 500
    assert discount_cents(CODES["SAVE10"], 0) == 0
