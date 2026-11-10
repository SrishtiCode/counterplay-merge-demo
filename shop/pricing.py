"""Prices in cents, so nothing is lost to rounding."""

TAX_RATE_PERCENT = 18


def format_price(cents: int) -> str:
    """1250 -> '€12.50'."""
    sign = "-" if cents < 0 else ""
    cents = abs(cents)
    return f"{sign}€{cents // 100}.{cents % 100:02d}"


def apply_discount(cents: int, percent: int) -> int:
    """The price after a discount of `percent`, rounded down to the cent."""
    if not 0 <= percent <= 100:
        raise ValueError("a discount is between 0 and 100 percent")
    return cents * (100 - percent) // 100


def with_tax(cents: int) -> int:
    """The price with tax added."""
    return cents + cents * TAX_RATE_PERCENT // 100
