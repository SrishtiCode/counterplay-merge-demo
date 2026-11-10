"""Formatting prices for display."""


def format_price(cents: int, symbol: str = "$") -> str:
    """A price in cents as text, like "$1,234.50" or "-$0.05"."""
    sign = "-" if cents < 0 else ""
    whole, rest = divmod(abs(cents), 100)
    return f"{sign}{symbol}{whole:,}.{rest:02d}"


def format_quantity(count: int, noun: str = "item") -> str:
    """A count with its noun, like "1 item" or "1,200 items"."""
    plural = noun if count == 1 else f"{noun}s"
    return f"{count:,} {plural}"
