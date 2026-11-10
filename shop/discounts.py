"""Discount codes and applying them to order totals."""

from dataclasses import dataclass
from datetime import date
from typing import Optional


class DiscountError(ValueError):
    """A discount code that can't be used."""


@dataclass(frozen=True)
class Discount:
    percent: int = 0
    amount_cents: int = 0
    min_total_cents: int = 0
    expires: date = date.max


CODES = {
    "SAVE10": Discount(percent=10, expires=date(2027, 6, 30)),
    "WELCOME5": Discount(amount_cents=500, min_total_cents=2000, expires=date(2027, 12, 31)),
}


def find_discount(code: str, today: date) -> Discount:
    """The discount for a code, refusing unknown or expired codes."""
    discount = CODES.get(code.strip().upper())
    if discount is None:
        raise DiscountError(f"Unknown discount code: {code!r}")
    if today > discount.expires:
        raise DiscountError(f"Discount code {code!r} expired on {discount.expires.isoformat()}")
    return discount


def discount_cents(discount: Discount, total_cents: int) -> int:
    """How much a discount takes off a total, never more than the total."""
    if total_cents <= discount.min_total_cents:
        return 0
    off = total_cents * discount.percent // 100 + discount.amount_cents
    return min(off, total_cents)


def apply_discount(total_cents: int, code: str, today: Optional[date] = None) -> int:
    """The total in cents after applying a discount code."""
    discount = find_discount(code, today or date.today())
    return total_cents - discount_cents(discount, total_cents)
